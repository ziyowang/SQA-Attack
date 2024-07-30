import numpy as np
import itertools
from time import time
from collections import defaultdict


def generate_observations(full_data_client, def_params, real_queries):
    """kw_id is the id wrt to this run (e.g., 0, 1, 2, ...nkw)
    keywords are ids wrt the original full dataset (i.e., they represent the actual keyword)
    We need gen_params to get ground truth queries (if any)
    """

    observations = {}
    traces = []
    dataset = full_data_client['dataset']
    keywords = np.array(full_data_client['keywords'])
    nkw = len(keywords)

    # Two ways of doing this, the second one is way faster!
    # First:
    # inverted_index = {kw_id: [doc_id for doc_id, doc_kws in enumerate(dataset) if keywords[kw_id] in doc_kws] for kw_id in range(nkw)}
    # Second:
    inverted_index = defaultdict(list)
    kw_to_kw_id = {kw: kw_id for kw_id, kw in enumerate(keywords)}
    for doc_id, doc_kws in enumerate(dataset):
        for kw in set(doc_kws) & set(keywords):
            inverted_index[kw_to_kw_id[kw]].append(doc_id)

    if def_params['name'] == 'none':

        trace_type = 'ap_unique'
        token_ids = np.random.permutation(np.max(real_queries) + 1)
        for kw_id in real_queries:
            traces.append((token_ids[kw_id], inverted_index[kw_id]))
        bw_overhead = 1
        real_and_dummy_queries = real_queries

    elif def_params['name'] == 'clrz':

        trace_type = 'ap_unique'
        token_ids = np.random.permutation(np.max(real_queries) + 1)
        tpr, fpr = def_params['tpr'], def_params['fpr']
        obf_inverted_index = {}
        for kw_id in range(nkw):
            coin_flips = np.random.rand(len(dataset))
            obf_inverted_index[kw_id] = [doc_id for doc_id, doc_kws in enumerate(dataset) if
                                         (keywords[kw_id] in doc_kws and coin_flips[doc_id] < tpr) or
                                         (keywords[kw_id] not in doc_kws and coin_flips[doc_id] < fpr)]

        ndocs_retrieved = 0
        ndocs_real = 0
        for kw_id in real_queries:
            traces.append((token_ids[kw_id], obf_inverted_index[kw_id]))
            ndocs_retrieved += len(obf_inverted_index[kw_id])
            ndocs_real += len(inverted_index[kw_id])
        bw_overhead = ndocs_retrieved / ndocs_real
        real_and_dummy_queries = real_queries

    else:
        raise ValueError("Defense {:s} not implemented".format(def_params['name']))

    observations['traces'] = traces
    observations['trace_type'] = trace_type
    observations['ndocs'] = len(dataset)

    return observations, bw_overhead, real_and_dummy_queries
class ObfuscatedResultExtractor(QueryResultExtractor):
    """Class that inherits the QueryResultExtractor and only add an access pattern obfuscation(=countermeasure).

    Ref: G.Chen, T.Lai, M.K.Reiter and Y. Zhang. Differentially private access patterns for searchable
    symmetric encryption. 2018.
    """

    def __init__(self, *args, m=6, p=0.88703, q=0.04416, **kwargs):
        """Initialize the obfuscator. The obfuscation parameters are those presented as
        optimal in the paper from Chen et al.
        """
        self.occ_array = np.array([])
        super().__init__(*args, **kwargs)
        self._p = p
        self._q = q
        self._m = m

        nrow, ncol = self.occ_array.shape
        self.occ_array = np.repeat(self.occ_array, self._m, axis=0)

        for i in range(nrow):
            for j in range(ncol):
                if self.occ_array[i, j]:  # Document i contains keyword j
                    if random.random() < self._p:
                        self.occ_array[i, j] = 0
                else:
                    if random.random() < self._q:
                        self.occ_array[i, j] = 1

    def __str__(self):
        return "Obfuscated"


class PaddedResultExtractor(QueryResultExtractor):
    """Class that inherits the QueryResultExtractor and only add an access pattern padding (=countermeasure).

    Ref: D.Cash, P.Grubbs, J.Perry and T. Ristenpart. Leakage-abuse attacks against searchable encryption. 2015
    """

    def __init__(self, *args, n=500, **kwargs):
        self.occ_array = np.array([])
        super().__init__(*args, **kwargs)
        self._n = n

        _, ncol = self.occ_array.shape
        self._number_real_entries = np.sum(self.occ_array)
        for j in range(ncol):
            nb_entries = sum(self.occ_array[:, j])
            nb_fake_entries_to_add = int(
                math.ceil(nb_entries / self._n) * self._n - nb_entries
            )
            possible_fake_entries = list(
                np.argwhere(self.occ_array[:, j] == 0).flatten()
            )
            if len(possible_fake_entries) < nb_fake_entries_to_add:
                # We need more documents to generate enough fake entries
                # So we generate fake document IDs
                fake_documents = np.zeros(
                    (nb_fake_entries_to_add - len(possible_fake_entries), ncol)
                )
                self.occ_array = np.concatenate((self.occ_array, fake_documents))
                possible_fake_entries = list(
                    np.argwhere(self.occ_array[:, j] == 0).flatten()
                )
            fake_entries = random.sample(possible_fake_entries, nb_fake_entries_to_add)
            self.occ_array[fake_entries, j] = 1

        self._number_observed_entries = np.sum(self.occ_array)
        logger.debug(
            f"Padding overhead: {self._number_observed_entries/self._number_real_entries}"
        )

    def __str__(self):
        return "Padded"
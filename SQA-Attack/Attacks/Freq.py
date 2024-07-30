
import numpy as np
from processing.process_obs import process_traces, compute_fobs
from processing.process_aux import get_faux
import numpy as np
from tqdm import tqdm
#from countermeasure import *
import time
from scipy.linalg import blas

class frequencyattack:
    def __init__(self,sim_Fre,real_Fre):
        self.sim_Fre=sim_Fre
        self.real_Fre=real_Fre
        #self.temp = {}
        self.tdid_2_kwsid={}
    def attack_fre(self):
        td_nb=len(self.real_Fre)
        #keyword_predictions_for_each_token={}
        for j in range(td_nb):
            self.tdid_2_kwsid[j] = np.argmin(np.abs(self.sim_Fre - self.real_Fre[j]))
        #temp={}
        #for i in range(td_nb):
         #   cost = np.abs(self.sim_Fre - self.real_Fre[int(self.real_Fre[i])])
          #  temp[int(self.real_Fre[i])]=np.argmin(cost)
           # self.tdid_2_kwsid=temp
        return self.tdid_2_kwsid
    #keyword_predictions_for_each_query = [keyword_predictions_for_each_token[token] for token in token_trace]
    #def recover_by_VF(self):
        # using volume and frequency to recover queries in td_list
        #tmp_pair = {}
       # for i in range(len(self.real_Fre)):
            #s1 = np.abs(self.sim_Vol - self.real_Vol[td_list[i]])
            #if self.without_Fre != True:
            #s2 = np.abs(self.sim_Fre - self.real_Fre[i])
            #s = self.alpha * s1 + (1 - self.alpha) * s2
            #else:
                #s = s1
            #tmp_pair[self.real_Fre[i]] = np.argmin(s)
       # return tmp_pair
   # def recover_by_VF(self, td_list):
        # using volume and frequency to recover queries in td_list
       # tmp_pair = {}
       # for i in range(len(td_list)):
            #s1 = np.abs(self.sim_Vol - self.real_Vol[td_list[i]])
           # if self.without_Fre != True:
              #  s2 = np.abs(self.sim_Fre - self.real_Fre[td_list[i]])
              #  s = self.alpha * s1 + (1 - self.alpha) * s2
         #   else:
          # #     s = s1
          #  tmp_pair[td_list[i]] = np.argmin(s)
     #   return tmp_pair
"""def find_closest(sim_fre, real_fre):
    result_contain_pkl = {}
    for real_value in real_fre:
        min_difference = float('inf')
        closest_sim_value = None
        for sim_value in sim_fre:
            difference = abs(real_value - sim_value)
            if difference < min_difference:
                min_difference = difference
                closest_sim_value = sim_value
        result_contain_pkl[real_value] = closest_sim_value
    return result_contain_pkl
sim_fre = [1, 2, 3, 4, 5]
real_fre = [2, 5, 7]

dictionary = find_closest(sim_fre, real_fre)
print(dictionary)
"""
def freq_attack(obs, aux, exp_params):
    def_params = exp_params.def_params

    token_trace, token_info = process_traces(obs, aux, def_params)
    n_tokens = len(token_info)
    fobs = compute_fobs(def_params['name'], token_trace, n_tokens)
    faux = get_faux(aux)

    keyword_predictions_for_each_token = {}
    for j in range(n_tokens):
        keyword_predictions_for_each_token[j] = np.argmin(np.abs(fobs[j] - faux))
    keyword_predictions_for_each_query = [keyword_predictions_for_each_token[token] for token in token_trace]

    return keyword_predictions_for_each_query

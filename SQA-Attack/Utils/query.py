"""
# Generate query with uniform distribution

query = np.random.choice(user_kws_universe, observed_query_number_per_week, replace=True, p=None)

# Generate query with Zipfian distribution
a=1
query = np.random.zipf(a, observed_query_number_per_week)
# Generate query with inverted Zipfian distribution
a=1
query = np.random.zipf(1/a, observed_query_number_per_week)
"""


import numpy as np

# 计算Zipfian分布的概率
def zipf_p(rank, s, N):
    return 1.0 / (rank ** s) / np.sum([1.0 / (i ** s) for i in range(1, N + 1)])
user_kws_universe=1
# 定义参数
s = 1.5  # Zipfian分布的参数
N = len(user_kws_universe)  # 词汇量的大小

# 生成服从Zipfian分布的查询
probabilities = np.array([zipf_p(rank, s, N) for rank in range(1, N + 1)])
query = np.random.choice(user_kws_universe, observed_query_number_per_week, replace=True, p=probabilities)

"""


# 定义参数
s = 1.5  # Zipfian分布的参数
N = len(user_kws_universe)  # 词汇量的大小

# 生成服从Zipfian分布的查询
query_indices = np.random.zipf(a=s, size=observed_query_number_per_week)
query_indices = np.minimum(query_indices, N-1)  # 确保查询索引不超过词汇量大小
query = user_kws_universe[query_indices]
# 定义参数
N = len(user_kws_universe)  # 词汇量的大小

# 生成服从Zipfian分布的查询
query_indices = np.random.zipf(a=s, size=observed_query_number_per_week)
query_indices = np.minimum(query_indices, N-1)  # 确保查询索引不超过词汇量大小
zipf_query = user_kws_universe[query_indices]

# 生成服从均匀分布的查询
uniform_query_indices = np.random.randint(0, N, size=observed_query_number_per_week)
uniform_query = user_kws_universe[uniform_query_indices]
"""
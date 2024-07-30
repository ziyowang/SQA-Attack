import pickle
import random

# Load the original pickle file
with open("path", "rb") as f:
    total_doc, kws_dict  = pickle.load(f)
    #print(total_doc)
    #print(kws_dict)

# Extract dataset and keyword_dict
#dataset = data['dataset']
#keyword_dict = data['keyword_dict']

# 假设你的数据集是一个列表，名为dataset
dataset =total_doc # 你的数据集
ratio = 30109 / 66491

# 计算需要选择的样本数量
half_of_dataset = int(ratio * len(dataset))

# 使用随机数生成器从数据集中随机选择一半的样本
random_sample = random.sample(dataset, half_of_dataset)

#print(random_sample)
# Calculate 50% of the dataset length

#half_length = len(dataset) // 2

# Randomly select 50% of the dataset
#random_dataset = random.sample(total_doc, int(ratio))
#print(random_dataset)

# Create a new dictionary to store the selected data and keyword_dict
#new_data = {'dataset': random_dataset, 'keyword_dict': keyword_dict}

# Save the new pickle file
with open("path", "wb") as f:
    pickle.dump([random_sample,kws_dict], f)
with open("path", "rb") as f:
    total_doc_reduced, kws_dict_reduced  = pickle.load(f)
    #print(kws_dict_reduced)
    print(total_doc_reduced)



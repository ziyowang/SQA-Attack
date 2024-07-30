def cal_g_index(real_Fre):

    g_index = 0
    sorted_td_frequency = []
    top_td_g_index = []
    for i in range(len(real_Fre)):
        sorted_td_frequency.append([i, real_Fre[i]])
    sorted_td_frequency.sort(key=lambda x: x[1], reverse=True)
    for i, (keyword, freq) in enumerate(sorted_td_frequency):
        if freq >= (i + 1) ** 2 and (i == len(sorted_td_frequency) - 1 or freq < (i + 2) ** 2):
            g_index = i + 1
    #top_td_g_index = [td for td, _ in sorted_td_frequency[:round(g_index)]]  # 这里有个小修改
    return round(g_index)
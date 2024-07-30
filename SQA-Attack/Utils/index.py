def abccc(kws_count,user_kws_universe_size):
    total_elements = len(kws_count)

    # 计算各个区域的大小
    high_freq_size = int(total_elements * 2 / 4)
    middle_size = int(total_elements * 1 / 4)
    last_size = total_elements - high_freq_size - middle_size

    # 根据总数和区域大小调整各个区域的大小
    if high_freq_size + middle_size + last_size < user_kws_universe_size:
        high_freq_size += user_kws_universe_size - (high_freq_size + middle_size + last_size)
    elif high_freq_size + middle_size + last_size > user_kws_universe_size:
        # 高频区域的大小超过了目标总数，需要适当减小
        high_freq_size -= high_freq_size + middle_size + last_size - user_kws_universe_size

    # 计算各个区域的起始和结束索引
    high_freq_start = 0
    high_freq_end = high_freq_start + high_freq_size
    middle_start = high_freq_end
    middle_end = middle_start + middle_size
    last_start = middle_end
    last_end = last_start + last_size

    # 从不同区域提取元素
    high_freq_elements = kws_count[high_freq_start:high_freq_end]
    middle_elements = kws_count[middle_start:middle_end]
    last_elements = kws_count[last_start:last_end]
    return high_freq_elements+middle_elements+last_elements

def m_convert(n): #數字國字轉換
    units = ['', '萬', '億']
    nums = ['零', '壹', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖']
    decimal_label = ['角', '分']
    small_int_label = ['', '拾', '佰', '仟']
    int_part = str(int(n))
    res = []
    # if decimal_part:
    #     res.append(''.join([nums[int(x)] + y for x, y in zip(decimal_part, decimal_label) if x != '0']))
    if int_part != '0':
        # res.append('圓')
        while int_part:
            small_int_part, int_part = int_part[-4:], int_part[:-4]
            tmp = ''.join([nums[int(x)] + (y if x != '0' else '') for x, y in list(zip(small_int_part[::-1], small_int_label))[::-1]])
            tmp = tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
            unit = units.pop(0)
            if tmp:
                tmp += unit
                res.append(tmp)
    return ''.join(res[::-1])

def d_convert(n): #數字日期轉換
    nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    small_int_label = ['', '十', '百', '千']
    int_part = str(int(n))
    res = []  
    if int_part != '0':
        while int_part:
            small_int_part, int_part = int_part[-4:], int_part[:-4]
            tmp = ''.join([nums[int(x)] + (y if x != '0' else '') for x, y in list(zip(small_int_part[::-1], small_int_label))[::-1]])
            tmp = tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
            if tmp:
                res.append(tmp)
    return ''.join(res[::-1])

def d32_convert(n): #小於32數字日期轉換
    nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九','十',
    '十一','十二','十三','十四','十五','十六','十七','十八','十九','二十',
    '二十一','二十二','二十三','二十四','二十五','二十六','二十七','二十八','二十九','三十',
    '三十一']

    num =nums[int(n)]
    return num


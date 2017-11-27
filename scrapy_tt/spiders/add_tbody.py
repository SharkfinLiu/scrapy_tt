import re
import itertools


def add_tbody(selector_css):
    add_tbody = ' tbody >'
    # 将table与非table拆分开
    css_re = re.compile(r'table[\-:()0-9a-zA-Z]*\s>')
    t = css_re.finditer(selector_css)
    star =[] #放table起始下标 ， 按顺序放置，下同
    end =[] #table结束下标
    for i in t:
        star.append(i.span()[0])
        end.append(i.span()[-1])
    list_len = len(star)
    #将拆分出来的table与非table分别放入table与other
    table = [] #放拆分出来的table
    other = [] #放拆分出来的非table
    other.append(selector_css[:star[0]])
    for i in range(list_len):
        if i <list_len-1:
            other.append(selector_css[end[i]:star[i+1]])
        table.append(selector_css[star[i]:end[i]])
    other.append(selector_css[end[-1]:])

    # 组合
    list1 = list(range(1,len(table)+1))
    # list1 = [1, 2, 3]
    list2 = []
    end = []
    for i in range(1, len(list1) + 1):
        iter = itertools.combinations(list1, i)
        list2.append(list(iter))
    for lis in list2:
        for li in lis:
            other_1 = other[:]
            table_1 = table[:]
            for i in list(li):
                table_1[i - 1] = table_1[i - 1] + add_tbody
            for i in range(len(other_1)):
                end.append(other_1[i])
                if i < len(table_1):
                    end.append(table_1[i])
            end.append(',')
    result = ''.join(end)
    result = selector_css + ',' + result
    return (result)
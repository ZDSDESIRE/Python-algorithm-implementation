'''
基数排序
'''

# 1、描述
'''
  基数排序（radix sort）是一种非比较型整数排序算法，属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort或bin sort)，
  顾名思义，它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用。
  其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
  基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
'''

# 2、算法步骤
'''

'''

# 3、代码实现
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j//(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

# 4、示例
arr = [10, 23, 6, 8, 2, 16, 0, 9]
print(radix_sort(arr))  # 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

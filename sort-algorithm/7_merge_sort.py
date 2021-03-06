'''
归并排序
'''

# 1、描述
'''
  归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
  归并排序的实现有两种方法：
    （1）自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
    （2）自下而上的迭代。
  将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
  归并过程为：
    比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；
    否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
    归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。
'''

# 2、算法步骤
'''
  （1）申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
  （2）设定两个指针，最初位置分别为两个已经排序序列的起始位置；
  （3）比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
  （4）重复步骤 3 直到某一指针达到序列尾；
  （5）将另一序列剩下的所有元素直接复制到合并序列尾。
'''

# 3、代码实现
# 归并
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr) // 2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)


# def mergeSort(arr):
#     import math
#     if(len(arr)<2):
#         return arr
#     middle = math.floor(len(arr)/2)
#     left, right = arr[0:middle], arr[middle:]
#     return merge(mergeSort(left), mergeSort(right))

# def merge(left,right):
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0));
#         else:
#             result.append(right.pop(0));
#     while left:
#         result.append(left.pop(0));
#     while right:
#         result.append(right.pop(0));
#     return result

# 4、示例
arr = [10, 23, 6, 8, 2, 16, 0, 9]
print(merge_sort(arr))  # 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

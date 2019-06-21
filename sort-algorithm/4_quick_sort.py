'''
快速排序

【描述】：
  通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据标出有序数列。
'''

# 代码实现
def quick_sort(ls):
  return q_sort(ls, 0, len(ls) - 1)  # 返回待排序列最小下标值 left 和最大下标值 right

def q_sort(ls, left, right):
  if left < right:
    pivot = q_partition(ls, left, right)  # 获取待排序列一个分组标准，并对其进行分组
    q_sort(ls, left, pivot - 1)
    q_sort(ls, pivot + 1, right)
  return ls

def q_partition(ls, left, right):
  pivotkey = ls[left]
  while left < right:
      while left < right and ls[right] >= pivotkey:
        right -= 1
      ls[left] = ls[right]
      while left < right and ls[left] <= pivotkey:
        left += 1
      ls[right] = ls[left]
  ls[right] = pivotkey
  return left

# 示例
list1 = [10, 23, 6, 8, 2, 16, 0, 9]
print(quick_sort(list1))
# 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

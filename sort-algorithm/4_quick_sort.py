'''
快速排序
'''

# 1、描述
'''
  快速排序是由东尼·霍尔所发展的一种排序算法。
  快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists），其是一种分而治之思想在排序算法上的典型应用。
  通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
  然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据标出有序数列。
'''

# 2、算法步骤
'''
  （1）从数列中挑出一个元素，称为 “基准”（pivot）;
  （2）重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
  在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
  （3）递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序，直至迭代（iteration）完成，即完成排序。
'''

# 3、代码实现
def quick_sort(arr):
  return q_sort(arr, 0, len(arr) - 1)  # 返回待排序列最小下标值 left 和最大下标值 right

def q_sort(arr, left, right):
  if left < right:
    pivot = q_partition(arr, left, right)  # 获取待排序列一个分组标准，并对其进行分组
    q_sort(arr, left, pivot - 1)
    q_sort(arr, pivot + 1, right)
  return arr

def q_partition(arr, left, right):
  pivot = left
  while left < right:
      while left < right and arr[right] >= arr[pivot]:
        right -= 1
      arr[left] = arr[right]
      while left < right and arr[left] <= arr[pivot]:
        left += 1
      arr[right] = arr[left]
  arr[right] = arr[pivot]
  return left

# 4、示例
arr = [10, 23, 6, 8, 2, 16, 0, 9]
print(quick_sort(arr))  # 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

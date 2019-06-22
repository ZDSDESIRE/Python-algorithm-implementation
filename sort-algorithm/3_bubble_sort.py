'''
3、冒泡排序

【描述】：
  它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
  走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
'''

# 代码实现
def bubble_sort(ls):
  count = len(ls)
  for i in range(0, count):
    for j in range(i + 1, count):
      if ls[i] > ls[j]:
        ls[i], ls[j] = ls[j], ls[i]
  return ls

# 示例
# 示例
list1 = [10, 23, 6, 8, 2, 16, 0, 9]
print(bubble_sort(list1))
# 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

'''
直接选择排序

【描述】：
  基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
  第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
  以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
'''
# 代码实现
def select_sort(ls):
  count = len(ls)
  for i in range(0, count):
    min = i
    for j in range(i + 1, count):
      if ls[min] > ls[j]:
        min = j
    ls[min], ls[i] = ls[i], ls[min]
  return ls

# 示例
list1 = [10, 23, 6, 8, 2, 16, 0, 9]
print(select_sort(list1))
# 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

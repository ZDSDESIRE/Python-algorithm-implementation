'''
2、希尔排序

【描述】：
  希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
  希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 
  希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
'''

# 代码实现
def shell_sort(ls):
  count = len(ls)
  step = 2
  gap = count // step  # Python2.2开始，"/"表示除法, 结果可能为浮点数，而"//"表示整除，结果不计小数部分，直接为整数
  while gap > 0:
    for i in range(0, gap):
      j = i + gap
      while j < count:
        k = j - gap
        key = ls[j]
        while k >= 0:
          if ls[k] > key:
            ls[k + gap] = ls[k]
            ls[k] = key
          k -= gap
        j += gap
    gap //= step
  return ls

# 示例
list1 = [10, 23, 6, 8, 2, 16, 0, 9]
print(shell_sort(list1))
# 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

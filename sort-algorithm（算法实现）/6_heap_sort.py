'''
堆排序
'''

# 1、描述
'''
  堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
  可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是近似完全二叉树的结构。
  大根堆：每个结点的值都大于或等于左右子结点，在堆排序算法中用于升序排列。
  小根堆：每个结点的值都小于或等于左右子结点，在堆排序算法中用于降序排列。
  大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
  在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
  堆排序的平均时间复杂度为 Ο(nlogn)。
'''

# 2、算法步骤
'''
  （1）创建一个堆 H[0……n-1]；
  （2）把堆首（最大值）和堆尾互换；
  （3）把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
  （4）重复步骤 2，直到堆的尺寸为 1。
'''


# 3、代码实现
# 【方法一】
# 原理：（1）根据待排序列构造一个大根堆；
# （2）取出这个大根堆的堆顶节点（最大值），与堆的最右下元素进行交换，然后把去掉最大值的剩余元素再构造成一个大根堆（重复第一步）；
# （3）重复第二步，知道这个大根堆的长度为1，此时即为完成排序。

# 利用链表结构 deque 将待排数组初始化成一个无序序列，再追加一个辅助位 "0"
def arr_deque(arr):
  from collections import deque
  L = deque(arr)
  L.appendleft(0)
  return L

# 堆排序
def heap_sort(arr):
  arr_length = len(arr)
  L = arr_deque(arr)
  first_sort_count = arr_length // 2
  for i in range(first_sort_count):
    heap_adjust(L, first_sort_count - i, arr_length)
  for i in range(arr_length - 1):
    swap_parameter(L, 1, arr_length - i)
    heap_adjust(L, 1, arr_length - i - 1)
  return [L[i] for i in range(1, len(L))]

# 交换元素
def swap_parameter(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# 堆调整
def heap_adjust(arr, start, end):
  temp = arr[start]
  i = start
  j = 2 * i
  while j <= end:
    if j < end and arr[j] < arr[j + 1]:
      j += 1
    if temp < arr[j]:
      arr[i] = arr[j]
      i = j
      j = 2 * i
    else:
      break
  arr[i] = temp

# 【方法二】
'''
# 创建大根堆
def build_max_Heap(arr):
    import math
    for i in range(math.floor(len(arr)/2), -1, -1):
        heapify(arr, i)

# 调整堆
def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap_parameter(arr, i, largest)
        heapify(arr, largest)

# 交换元素
def swap_parameter(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 堆排序
def heap_sort(arr):
    global arrLen
    arrLen = len(arr)
    build_max_Heap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap_parameter(arr, 0, i)
        arrLen -=1
        heapify(arr, 0)
    return arr
'''

# 【方法三】 Ps：有错误，暂未修改
'''
# 调整堆
def adjust_heap(arr, i, count):
  lChild = 2 * i + 1
  rChild = 2 * i + 2
  max = i
  gap = count / 2
  if i < gap:
    if lChild < count and arr[lChild] > arr[max]:
      max = lChild
    if rChild < count and arr[rChild] > arr[max]:
      max = rChild
    if max != i:
      arr[max], arr[i] = arr[i], arr[max]
      adjust_heap(arr, max, count)

# 创建堆
def build_heap(arr, count):
  gap = count / 2
  # while gap > 0:
  for i in range(0, gap)[::-1]:  # [::-1]表示读取从后向前（相反）的元素；[-1]表示读取最后一个元素；[:-1]表示读取除最后一个的全部元素；[2::-1]表示获取从下标为2的元素开始翻转读取。
    adjust_heap(arr, i, count)

# 堆排序
def heap_sort(arr):
  count = len(arr)
  build_heap(arr, count)
  for i in range(0, count)[::-1]:
    arr[0], arr[i] = arr[i], arr[0]
    adjust_heap(arr, 0, i)
'''

# 示例
arr = [10, 23, 6, 8, 2, 16, 0, 9]
print(heap_sort(arr))  # 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]

# Python-algorithm-implementation

## 基于Python的各类算法实现

***Sort-algorithm*&ensp;八大排序算法**

*1、[insert_sort &ensp;插入排序](sort-algorithm/1_insert_sort.py)*

* 插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。其基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，该算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。
* 插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
* 插入排序是一种优化算法，叫做拆半插入。

![insertionSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/insertionSort.gif)

*2、[shell_sort &ensp;希尔排序](sort-algorithm/2_shell_sort.py)*

* 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高&效的改进版本。
* 希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
* 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

*3、[bubble_sort &ensp;冒泡排序](sort-algorithm/3_bubble_sort.py)*

* 冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
* 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
* 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

![bubbleSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/bubbleSort.gif)

*4、[quick_sort &ensp;快速排序](sort-algorithm/4_quick_sort.py)*

* 快速排序是由东尼·霍尔所发展的一种排序算法。
* 快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists），其是一种分而治之思想在排序算法上的典型应用。
* 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据标出有序数列。

![quickSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/quickSort.gif)

*5、[select_sort &ensp;选择排序](sort-algorithm/5_select_sort.py)*

* 选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。
* 基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
* 第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
* 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。

![selectionSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/selectionSort.gif)

*6、[heap_sort &ensp;堆排序](sort-algorithm/6_heap_sort.py)*

* 堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。堆排序的平均时间复杂度为 Ο(nlogn)。
* 堆分为大根堆和小根堆，是近似完全二叉树的结构。
  大根堆：每个结点的值都大于或等于左右子结点，在堆排序算法中用于升序排列。
  小根堆：每个结点的值都小于或等于左右子结点，在堆排序算法中用于降序排列。
* 大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
  在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
  
![heapSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/heapSort.gif)

*7、[merge_sort &ensp;归并排序](sort-algorithm/7_merge_sort.py)*

* 归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
* 归并排序的实现有两种方法：
  （1）自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
  （2）自下而上的迭代。
* 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
  归并过程为：
  &ensp;&ensp;比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。
* 归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。

![mergeSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/mergeSort.gif)

*8、[radix_sort &ensp;基数排序](sort-algorithm/8_radix_sort.py)*

* 基数排序（radix sort）是一种非比较型整数排序算法，属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort或bin sort)，顾名思义，它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用。
* 其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
* 基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。

![radixSort](https://github.com/zone1240/Python-algorithm-implementation/raw/master/sort-algorithm/img/radixSort.gif)

<font color=#FF0000>注：</font>

* 以上算法原理动图均取自[JS-Sorting-Algorithm（十大经典排序算法）](https://github.com/hustcc/JS-Sorting-Algorithm.git)
* 关于算法的具体实现方法可参考对应的源码文件

- - -
***待补充 ...***

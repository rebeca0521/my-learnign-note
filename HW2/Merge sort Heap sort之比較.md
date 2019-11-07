# Merge sort / Heap sort之比較
## Merge sort介紹
* Divide and Conquer algorithm.
* 將數列分割到剩下一個元素
* 再兩兩合併，並在合併的時候進行排序
* 重複合併和排序動作，直到最後合併成一個數列就完成排序了

![](https://qph.fs.quoracdn.net/main-qimg-567496127084e388f88b84cfe00fa3db)

## Heap sort介紹
* 利用在資料結構中**二元樹**的堆積樹來做資料排序
* 分為 Max-heap、Min-heap
![](https://i.imgur.com/cw2h4Le.gif)
* 排序步驟
    1. 將數列排成Max heap
    2. 把root節點的資料移到已排序的陣列
    3. 移除一顆 heap tree 的節點
    4. 最後一個節點來補上被移除的節點
    5. Heapify(把樹轉乘Max heap)

![](https://i.imgur.com/Q4R7EzU.gif)





## 比較
### **Heap Sort:**
It is the slowest of the O(nlogn) sorting algorithms but unlike merge and quick sort it does not require massive recursion or multiple arrays to work.
### **Merge Sort:**
The merge sort is slightly faster than the heap sort for larger sets, but it requires twice the memory of the heap sort because of the second array.



### 比較表
|          | Merge sort | Heap sort |
| -------- |   -------- | -------- |
| 時間複雜度 | O(nlog2n)     | O(nlog2n)     |
| 額外空間 | O(n)     | O(1)     |
| 穩定    | stable    | unstable     |

### 比較圖
![](https://i.imgur.com/IAv2qe9.png)



## 補充
### 穩定排序(stable)

排序演算法分為穩定(Stable)和不穩定(Unstable)兩種，是指當資料中有相等數值的兩元素，經過排序之後是否能夠保持原有的相對位置。
>例如:
60 , 20 , **60** , 90
排序完會有兩種情況
20 , 60 , **60** , 90
20 , **60** , 60 , 90
第一種情況60和**60**和原始的相對位置一致(60在前)
能夠總是維持相對位置的排序法我們稱之為穩定排序，反之則稱為不穩定排序，不能確保相對位置與原來一樣(但是也有可能一樣)。


## Reference
> http://www-cs-students.stanford.edu/~rashmi/projects/Sorting.pdf

> http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm

> https://emn178.pixnet.net/blog/post/93671868

> https://jason-chen-1992.weebly.com/home/selection-merge-heap

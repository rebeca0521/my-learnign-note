# 作業
### [code](https://github.com/rebeca0521/my-learning-note/blob/master/4.%20Quick%20sort/HW_Quick%20sort.ipynb)
 
### 流程圖 
 ![](https://github.com/rebeca0521/my-learning-note/blob/master/4.%20Quick%20sort/S__3702915.jpg)
 
 
###### tags: `資料結構` `Quick sort`
# Quick sort
* Quick sort是一種把大問題分成小問題的Divide and Conquer方法
* 步驟如下:
    1. 在數列中隨機選一pivot
    2. 將數值比pivot小的放到左邊，數值比pivot大的放到右邊
    3. 左右兩邊都形成一新數列，且從1.步驟開始重複操作
    4. 直至無法再區分
    
![](https://i.imgur.com/O1sfyFy.png)

## 複雜度

* 時間複雜度

| Best | Average | Worst|
| ------|--------|------|
|NlogN | O(n*log n) | O(n^2) |

* 空間複雜度
O(n*log n)


## 原地（in-place）分割的版本
* 這個方法可以令我們不需要為子數列申請新的記憶體空間，使得每次遞回呼叫都僅需要 O(1) 的空間複雜度。
* 它僅僅需要切割的操作，不必再有合併的操作。
* 在切割時就也做完合併了。
* 步驟:
    >   1.從數列找出一個元素作為 pivot
        2.將 pivot 移動到數列末端
        3.設定一個指標指向數列前端，用來記錄小於 pivot 的元素的放置位置
        4.接下來開始遍歷所有元素（除了 pivot）
        5.若當前元素小於 pivot，就將該元素換到指標所指向的位置，且將指標往下一個位置移動
        6.若當前元素大於等於 pivot 則跳過不做任何動作
        7.當所有元素遍歷後，再將 pivot 與指標作指向的最後一個位置的元素交換
* 在 step 7 之前，原數列就已經被分為兩堆，前面那堆都是小於 pivot 的，而後面那堆都是大於等於 pivot 的。

![](https://i.imgur.com/zLuz1ln.png)




## pivot之選擇
* quick sort的時間複雜度關鍵在於選擇pivot。

* **固定選擇一位置**
  ex:第一個、最後一個數值、中間的數值
  但此法不是很好，可能選到不好的，有點在賭運氣。
* **亂數**
  但此法依然不是很好，可能選到不好的，有點在賭運氣。
* **midian-of-Three**
  挑選數列的第一個、中間的、及最後一個元素而用這三個之中的中位數  (median) 來當做 pivot。
* **median of medians**
  數列依大小排列，挑選位置在最中間的數值，雖是最好的方法，但不容易計算，反而會增加複雜度。








## Reference
> http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
> https://blog.kuoe0.tw/posts/2013/03/15/sort-about-quick-sort/


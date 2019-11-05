# Heap sort 說明

## 流程圖
1. Heapify : 將list形成的二元樹中的每個子樹排序調整成父節點會大於兩個子節點的樣子。
2. Heap sort : 在排序的時候會搭配著Heapify，把每一次調整完的根結點(Max num)和最後一個節點交換，再把Max num丟到另一個list中，直到無法再做heapify。
![](https://i.imgur.com/xhDx7X9.jpg)
![](https://i.imgur.com/HOy4ONo.jpg)
![](https://i.imgur.com/vRQwppu.jpg)
![](https://i.imgur.com/oheUKDF.jpg)


## 學習歷程
### 碰到的問題
* 跑迴圈時一直index out of list
* 不知道在子樹比較完後，如何反覆往上比在往下比

### 解決方法
在開始寫的程式碼時，有搭配一些簡單的小圖，所以程式碼的部分也稍微簡單一點，但發現會有很多問題，後來我是把圖的list設計複雜一點，再去想要怎麼解決，上面提到的兩個問題，整個重新改過後才發現，左右子節點的index部分不要分開寫會比較好，再加上maxindex這個變數，才能保持i不會跳來跳去。
第二個問題的部分，一開始我也有想從i=0或是i=最後一個index開始排序的兩個版本，但發現都無法寫出重複往上往下確認大小的的部分，後來參考網路上資料的流程圖，才發現重複查找可能要分開寫，而且分開寫也會讓我比較清楚，但我覺得幫助最大的還是把圖畫出來，才能比較好找出問題。







## Reference
> https://www.c-programming-simple-steps.com/heap-sort.html
> https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p

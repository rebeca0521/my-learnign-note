
# BST新增、查詢、修改、刪除
## 新增insert
insert應該是整個功能中最好想出來的
* 程式碼邏輯:
1. 先設一個current代表root
2. 把要insert的val和current的val比較
3. 若val小於current且current的left存在，current往left走一格變成current.left
4. 若val大於current且current的right存在，current往right走一格變成current.right
5. 重複2.~4.直到current的下一個left或right為None就insert進去

我是用迴圈方法執行，不是遞迴，但遞迴好像可以更精簡，之後再去改善!
## 查詢search
* 程式碼邏輯 :
1. 首先也是設一個current指向root
2. 再設一個pre代表前一個current
3. 要search的val和current的val比較是否一樣
4. 若不一致的話，比較val是大於還小於current，若小於current往左走，若大於current往右走
5. 直到current.val和要尋找的val一致即返回current


## 刪除delete
delete真的是花了我爆多時間
* delete的三種情況
    1.沒有子樹
    2.一個子樹
    3.兩個子樹

* 程式碼邏輯 : 
1. 先用search尋找要delete的target存不存在
2. 若存在，由於要把樹裡符合target的node都刪除，因此設定一個迴圈，只要target還被search的到就繼續跑下面的程序
3. 找到以後，先看看target右邊有沒有node，若存在node就找到右子樹中值最小的node去替換target，target的parent會指向替換的node，替換的node會指向target的child
4. 若沒找到，就看看左邊是否存在node，若存在node就找到左子樹中值最大的node去替換target，target的parent會指向替換的node，替換的node會指向target的child
6. 若都沒有子樹，就直接刪除
7. 最後再將樹平衡

上面步驟中有一些小細節要注意:
* 要設定一個pre去記住target的parent，因此我把pre就先寫在search裡面，以便delete可以直接使用。
* 在找右子樹中的最小值時，有可能發生最小值node和他parent的值一樣，若發生這種狀況，我會將target的左子樹直接接到右邊最小值node的左邊。

#### 示意圖
![](https://i.imgur.com/imoJwEQ.jpg)


## 修改modify
* 邏輯:
1. 先delete要被修改的target
2. insert進新的node
3. 平衡樹

上面步驟中有一些小細節要注意:
* 由於必須知道被delete的target有幾個，才知道要insert幾個新node，因此我在delete內新增一個變數，讓變數記住target被delete的次數，最後再insert
* 平衡樹的部分，我的方法是先把1、2步做完產生的樹裡得node值，丟到一個list裡，把list由小到大排序，list最中間的值會先被insert進去當作新root，再把list拆成左右兩邊的小list，小list也是insert最中間的值進新的Tree，繼續遞迴直到無法再拆成左右。
#### 示意圖
![](https://i.imgur.com/w9i4AEN.jpg)


# Reference
這是我程式碼的邏輯和一些解釋，所以沒有參考資料。

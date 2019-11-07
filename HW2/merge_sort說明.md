# Merge sort 說明

## 流程圖
* **size**:為每次排序前的list大小 (ex.兩數值要排序合併時size=1，四數值要排序合併時size=4)
* **L** : 為一指針指向每次要排序的數值左邊的index
* **R** : 為一指針指向每次要排序的數值右邊的index
* **newarr** : 為每次排序完所放入的新array
* **R_plus_num** : 為每一次R+1時，紀錄+的次數
* **L_plus_num** : 為每一次L+1時，紀錄+的次數


![](https://i.imgur.com/cMk3qGs.png)

## 學習歷程
### 碰到的問題
* 分割完如何合併
* 分割完要放到新的list還是交換位置
### 解決方法
一開始想說分割完ㄟˊ?不對阿只跑得出來一個值，經過賴永琪同學跟我說是用隔板的概念隔開，有如醍醐灌頂，我就用指針的概念再去做比較分割，在做merge sort得時候，我是邊想邊畫流程圖，再去想各種琪況，哪裡會有漏洞，幾乎是到最後才把程式碼打出來的。剛開始打出來得時後發現只跑出來兩個值，我就丟到spyder debuge才發現中間有些邏輯會讓他跑錯，由此再去修改流程圖和程式碼，最後就有成功跑出來了。
收穫是，我覺得邊畫流程圖邊想，真的比一開始就打code有效率很多，雖然我也想了很久，但是如果一開始打code可能邏輯上就會更亂(之前就是這樣)，邊畫邊想真的幫助我很多。
## Reference
> 1. 賴永琪(06170108)提點
> 2. https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.p

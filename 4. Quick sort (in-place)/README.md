# Quick sort in-place版本

## 概念
in-place版本和一般的quick sort不太一樣得地方是，一般的quick sort需要再增加兩個list，就會需要額外的儲存空間，額外需要的記憶體空間組態，在實際上的實作，也會極度影響速度和快取的效能，而in-place版的排序就只要在原本的array中就能完成。

## 步驟
![](https://i.imgur.com/jYdc0ZM.jpg)

1. 圖中第一步為原始的array，並且有兩個只針i和j，同時指向第一個值(index=0)
2. j會從第一個開始查看每一個index內的值，直到找到比pivot小的值就會停下來，與i指針所指的值進行swap(i只會指到大於pivot的值)
3. swap後，i和j都會+1，繼續找尋下一個小於pivot的值
4. 接著重複，直到所有值都被查看過
...
7. 第七個步驟為，最後i的值會和pivot交換位置，此時便可以看出pivot左邊都是小於pivot的值，而右邊都是大於pivot的值，左右兩邊再從1重複進行，直到不能再比較。

## code



## Reference
> https://www.youtube.com/watch?v=MZaf_9IZCrc
> https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort)
> https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F#%E5%8E%9F%E5%9C%B0%EF%BC%88in-place%EF%BC%89%E5%88%86%E5%89%B2%E7%9A%84%E7%89%88%E6%9C%AC

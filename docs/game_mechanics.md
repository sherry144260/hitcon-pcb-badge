# 設備數量
15-20個基地台
基地台和Badge可雙向溝通

# 遊戲機制

## 遊戲機制簡介
1. 一開始所有都是中立塔台，中立塔台需要分數達到一定程度才會被佔領
    - 塔台數值：設定分數下限 & 上限，中間有一區間會判定為中立塔台。EX: -1000 ~ 1000, 中間-50~50為中立值
3. 會眾透過遊戲、互動取得分數，分數可以用以攻擊/防禦塔台 (要加 or 減塔的數值，會眾可以自己決定要使用多少分數)
4. 塔台數值會隨時間下降，因此已經被佔領的塔台，若有一段時間都沒有人去加減分數，會回到中立塔台

待確認：
1. 有鑽漏洞(讓會眾玩Hacking)的機制嗎
2. 可以當內鬼?
~~3. 有沒有台主？~~

## 取得分數的方法
* 站在塔台旁邊搖晃Badge
* ReCTF：解題可以一次增加更多分數
* 小遊戲對戰：Dino, Snake, Tetris
* 贊助商活動

## 遊戲結算
* 佔領塔數贏的那隊獲勝 (獎品待確認)

## 記分板
* 個人已經輸出過的分數
* 地圖：各地佔領情況，分數差異

# TokenPriceTracker_DiscordBot
CoinMarketCapにリスティングされているコイン価格をトラッキングすることができます。

# 使用方法
**基本的にBotのアクティビティ欄にコインの価格が表示されます。**
![IMG_2201](https://github.com/yblockcha1n/TokenPriceTracker_DiscordBot/assets/144770048/7701601e-84cd-4447-a15f-5c92feaeb8dd)
これは標準で**1分毎**に更新するようにコーディングしており、API枠を節約したい方は任意の時間に変更してください。

`@tasks.loop(minutes=1) #更新/1分`

また、`/chart 〇〇`とコマンドをDiscordチャンネルに打ち込むことで、コインの価格が返答されます。
※〇〇は指定したコインシンボルを入力してください。
https://github.com/yblockcha1n/TokenPriceTracker_DiscordBot/assets/144770048/f62e6704-26bf-40b0-9d8e-dedafbb9ae1f

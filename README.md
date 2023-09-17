# TokenPriceTracker_DiscordBot
CoinMarketCapにリスティングされているコイン価格をトラッキングすることができます。

# 使用方法
**基本的にBotのアクティビティ欄にコインの価格が表示されます。**
![IMG_2201](https://github.com/yblockcha1n/TokenPriceTracker_DiscordBot/assets/144770048/7701601e-84cd-4447-a15f-5c92feaeb8dd)

これは標準で**1分毎**に更新するようにコーディングしており、API枠を節約したい方は任意の時間に変更してください。

`@tasks.loop(minutes=1) #更新/1分`

また、`/chart 〇〇`とコマンドをDiscordチャンネルに打ち込むことで、コインの価格が返答されます。
※〇〇は指定したコインシンボルを入力してください。
![Screen-Recording-2023-09-18-at-0 54 28](https://github.com/yblockcha1n/TokenPriceTracker_DiscordBot/assets/144770048/444b5715-a415-477c-a849-088a3d9fe25b)

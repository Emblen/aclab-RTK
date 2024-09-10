# u-centerで得たRTKデータを国家座標に変換する

## 準備
- **プログラムファイル(.py)**  
  https://github.com/Emblen/aclab-RTK の Code -> Download ZIP でローカルにダウンロードして解凍する
  
- **u-centerのテキストコンソールの出力をコピペした.txtファイル**  
u-centerのテキストコンソールでこのようなテキストデータを得ることができるので，`hogehoge.txt`（ファイル名は自由）のようにテキストファイルを作成する
```
10:16:56  $GNGGA,101656.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*55
10:16:57  $GNGGA,101657.00,3606.67500,N,14006.33666,E,4,12,0.60,75.7,M,39.1,M,1.0,0004*56
10:16:58  $GNGGA,101658.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*59
10:16:59  $GNGGA,101659.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*58
10:17:00  $GNGGA,101700.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*55
10:17:01  $GNGGA,101701.00,3606.67500,N,14006.33666,E,4,12,0.60,75.7,M,39.1,M,1.0,0004*54
10:17:02  $GNGGA,101702.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*57
10:17:03  $GNGGA,101703.00,3606.67500,N,14006.33666,E,4,12,0.60,75.6,M,39.1,M,1.0,0004*57
```
- **Python実行環境**  
  WindowsならMicroSoft Storeから検索窓に'python'と入力すると出てくる．バージョンはどれでもいいが，できるだけ最新のバージョンが好ましい．
  
- **プログラムの実行に必要なライブラリ** 
  コマンドプロンプトで以下を一行ずつ実行する．
  ```
  pip install numpy　　
  pip install click
  ```
## ディレクトリ構成
※必ずしもこの通りでなくてもよいが，プログラム実行時の引数に注意
```
|--aclab-RTK
   |--src (ソースコードがあるディレクトリ)
   |  |--to_decimal_xy.py
   |  `--calc_xy.py
   |--outputdir (プログラム実行時に設定するディレクトリ名)
   |  |--hogehoge1_xy.txt (時刻と国家座標を格納したテキストファイル)
   |  |--hogehoge2_xy.txt
   |  ...
   |--txtdir (プログラム実行時に設定するディレクトリ名）
   |  |--hogehoge1.txt (u-centerのテキストコンソールの出力をコピペしたものたち)
   |  |--hogehoge2.txt
   |  ...
```
# プログラムの実行
`aclab-RTK`ディレクトリに移動し，コマンドプロンプト等で  
`python src/to_decimal_xy.py --txtdir txtdir --outdir outputdir`  
を実行する．outputdir/以下に国家座標に変換されたRTKデータが姿を現す．

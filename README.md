# food101-cloudml
Food-101データセットによる分類をGoogle Cloud Machine Learningで実行します。

## 環境構築

Python3を使用します。

ライブラリのインストール。
```
% pip3 --user tensorflow-gpu==1.10.0 opencv-python h5py
```
TensorFlow バージョン1.8と1.10で動作確認しています。

gcloudコマンドとgsutilコマンドを使えるようにします。  
https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction?hl=ja

## 使用手順

Food-101データセットをダウンロードし、ついでに検証用の縮小画像を作ります。
```
% ./download.sh
```
学習を行います。GTX 1050 Tiで12時間ほどかかります。
```
% python3 train.py
```
SavedModelを作成します。
```
% python3 keras2saved_model.py
```

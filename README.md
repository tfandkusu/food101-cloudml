# food101-cloudml
[Food-101](https://www.vision.ee.ethz.ch/datasets_extra/food-101/)データセットによる分類をGoogle Cloud Machine Learningで実行します。

## 環境構築

Python3を使用します。

ライブラリのインストール。
```
% pip3 --user tensorflow-gpu==1.10.0 opencv-python h5py google-api-python-client
```
TensorFlow バージョン1.8と1.10で動作確認しています。

gcloudコマンドとgsutilコマンドを使えるようにします。  
https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction?hl=ja  
環境変数 GOOGLE_APPLICATION_CREDENTIALS の設定まで完了してください。

## 使用手順

Food-101データセットをダウンロードし、ついでに検証用の縮小画像を作ります。
```
% ./download.sh
```
学習を行います。GTX 1050 Tiで12時間ほどかかります。
```
% python3 train.py
```
予測精度を確認します。だいたい60%ぐらいになります。
```
% python3 evaluate.py
```
SavedModelを作成します。
```
% python3 keras2saved_model.py
```
Google Cloud Storageのバケット名を deplay.sh に設定します。全体で一意である必要があります。  
Cloud MLにデプロイします。
```
% ./deploy.sh
```
request.py の PROJECT_ID にご使用のプロジェクトIDを設定してください。
クラウドに対して予測を実行します。
```
% python3 request.py
```

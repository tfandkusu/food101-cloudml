#!/bin/sh
# SavedModelを保存するバケット名。一意の名前を設定してください。
BUCKET_NAME="yout_bucket_name"
# モデル名
MODEL_NAME=food101
# バケットを作成
gsutil mb -c regional -l us-central1 gs://$BUCKET_NAME/
# バケットにSavedModelを保存
gsutil cp -r saved_model/* gs://$BUCKET_NAME/saved_model/
# CloudMLのモデルを作成
gcloud ml-engine models create $MODEL_NAME
# CloudMLのバージョンを作成
gcloud ml-engine versions create "v1" --model $MODEL_NAME \
--origin gs://$BUCKET_NAME/saved_model \
--python-version 3.5 \
--runtime-version 1.10

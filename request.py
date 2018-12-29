from googleapiclient import discovery
import cv2
import numpy as np
import json
import base64

PROJECT_ID='your_project_id'
MODEL_NAME='food101'

#ラベル一覧
with open('labels.txt') as f:
    labels = []
    for line in f.readlines():
        line = line.rstrip()
        labels.append(line)
# サービスを取得
service = discovery.build('ml','v1')
# POSTするパスを生成
name = "projects/%s/models/%s/versions/%s" % (PROJECT_ID, MODEL_NAME,"v1")
# テストファイル
path = "shrink/chicken_wings/1036790.jpg"
# 入力データを作成
x = cv2.imread(path,cv2.IMREAD_COLOR)
ret,x = cv2.imencode(".png",x)
x = x.tostring()
# ポストするJSONを作成
obj = {'instances' : [{'input' : {"b64": base64.b64encode(x).decode('utf-8')}}]}
# ポストする
response = service.projects().predict(name=name,body=obj).execute()
# 結果から分類結果を得る
output = np.array(response['predictions'][0]['output'])
# numpyのarrayを見やすい表示形式にする
np.set_printoptions(precision=4,suppress=True)
print("出力")
print(output)
index = output.argmax()
print("一番大きいのは%d番目" % index)
print("%d番目の料理は %s" % (index,labels[index]))

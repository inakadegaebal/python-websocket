概要
===========
ブラウザでチャットができるサンプルソース

前提条件(ざっくり)
===========
・Python3  
・websockets https://pypi.org/project/websockets/

※以下のコマンドはMac基準    

インストール
===========
```
% git clone https://gitlab.efactoryguys.com/JEONG/python-websocket.git
% cd python-websocket
% python3 -m venv venv
% . venv/bin/activate
(venv) % pip install websockets
```

動作確認
===========
1. ターミナルでサーバー起動
```
(venv) % python3 server.py
```
2. Windowsエクスプローラー or MacFinder等でindex.htmlを実行
```
例えば
file:///Users/jeong/dev/python-websocket/index.html
```
3. 別のブラウザでindex.htmlを実行
4. 各ブラウザでConnect後、メッセージを送信(Send)してみる
# 株売買シミュレーション
![stock_simulation_description](https://github.com/999yo/stock_simulation_app/assets/103639076/4e2c8003-b4f1-423a-9dba-e069ef37ee9f)

## **アプリURL**
https://appdjangostock.pythonanywhere.com/home/
## テストアカウント
ユーザー名: stock  
パスワード: simulation
## アプリを作ったキッカケ
私は株式投資で損失のリスクを考えずに株を購入してしまうことがあります。  
そして大きな損失を抱えた苦い経験もあります。  
計画的な投資を行うために、購入する前にあらかじめ損失額を把握しておくアプリを作ってみました。  
また、アプリ上は架空の売買なので、お金を使うことなく株式投資の練習にも使えます。  
2024年から新NISAも開始されるので、ぜひ株式投資の勉強の一歩にこのアプリを使ってみてください。　　

## 実装した機能
- ログイン機能   
- 証券コードから、現在の株価（前日の終値）の情報を取得する機能   
- ユーザーが設定したシミュレーション株価で損益を計算する機能  
- 平均取得単価から、5~30%株価が下落した際の株価と損失額を計算する機能
- 計算結果を記録する機能  
- 保存したデータをリスト化し表示する機能  
- 保存したデータの株の現在の損失益を計算する機能。

## 機能イメージ
| 未ログイン トップページ | 計算&データ保存| 保存データ閲覧 |
|:-----------:|:------------:|:------------:|
|![toppage-1](https://github.com/999yo/stock_simulation_app/assets/103639076/2a6248aa-dee0-4df8-9a9d-48a76172ed3e)|![stock_simulation](https://github.com/999yo/stock_simulation_app/assets/103639076/83a374bf-7d88-4503-8a90-63720645a741)|![simulation_list-0](https://github.com/999yo/stock_simulation_app/assets/103639076/da316a13-947d-4fc8-8e4c-72f68f7f1124)|
| ログインしてなくても計算機能を使えるようにしました。 | ログインすると計算結果が保存できます。| 保存したデータをリスト化して閲覧できます。 |

| アプリ説明（About）| 
|:-----------:|
|<img src="https://github.com/999yo/stock_simulation_app/assets/103639076/53b8d415-dda6-4aaf-8275-498920f8617f" width="50%">|
| アプリ内にあるAboutページにてアプリの説明・機能を画像で紹介しています。画像の表示はjQueryの機能を使用してます。|

| アカウント登録 | ログイン| ユーザー情報閲覧 |
|:-----------:|:------------:|:------------:|
|![signup-0](https://github.com/999yo/stock_simulation_app/assets/103639076/6c5dfb8b-9994-4483-b25d-29554bb474c0)|![Login-0](https://github.com/999yo/stock_simulation_app/assets/103639076/1e7546a0-faa2-461c-bc9f-750996a6e069)|![user_info-0](https://github.com/999yo/stock_simulation_app/assets/103639076/c4e8e22b-3f8f-48e0-a643-c89f81dc0e1b)|




## 使用技術
| カテゴリ       | 技術  |
| :-------------: | :------------: |
|フロントエンド | CSS　JavaScript（jQuery） boostrap5|
|バックエンド   | Python 3.7.13　  Django 3.2.23 |
| データベース   |  MySQL 8.0.33  |
|ライブラリ　　 |  yahoo-finance-api2 0.0.12    |

## ER図
<img src="https://github.com/999yo/stock_simulation_app/assets/103639076/c0fd853a-c943-47ae-92b7-b8e0b6c42e6c" width="50%">

## 今後追加したい機能
- 証券コードより現在株価だけでなく企業名も取得する機能  
- 計算結果がでたときに、チャートライン等の図を表示する機能
- 空売りによるトレードの損益を計算する機能











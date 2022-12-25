# Line pressuretest
# 目標:做出積分制的壓力測驗
用選項按鈕製作出3種10題壓力測驗的題目
# 構想:
原本是想做只有選擇的機器人，但後來又想要加入計算分數的系統進去，為了讓返回上一題的分數正確，所以我將不同題目的分數用不同的名詞代替，這樣的話點選上一題那上一題的分數就會歸0
這樣再重新做選擇分數即會正常除此之外每次做完後會自動把每一題得到的分數歸零以便重新開始
# 環境架設
python3.9

pip install pipenv

pipenv --three

pipenv install flask

pipenv install line-bot-sdk

下載ngrok將ngrok放到目標資料夾，在Vscode cmd輸入ngrok http 5000來連接ngrok，將ngrok產生的網址放置line developers
![螢幕擷取畫面 2022-12-22 213153](https://user-images.githubusercontent.com/120545242/209145362-02f52a04-4fa2-4bcd-ae1a-67b7d6798a1f.png)
![11111](https://user-images.githubusercontent.com/120545242/209146217-abe64db4-e106-45f3-924c-ee0013626704.png)
接著到powershell 輸入pipenv shell進入後輸入python app.py執行程式接著回到line developers verify功能即可運作
# 我的fsm
![fsm](https://user-images.githubusercontent.com/120545242/209461998-938d0d84-39ff-498c-a290-7b7dfe764a56.png)

# 使用方式
加入好友後，執行程式，輸入開始即可選擇要做的測驗種類

![888888888](https://user-images.githubusercontent.com/120545242/209458412-bd0ca6a6-9973-44a6-9036-1b7dccdbe523.png)

選擇第一題後會跳到第二題，從第二題開始會有返回上一題的選項，點選後會回到上一題再繼續做選擇

![333333](https://user-images.githubusercontent.com/120545242/209147901-2164e0ec-7647-47b2-8348-3d713f63bff4.png)

做完十題後，點選結果，會根據你選擇的選項進行加分最後給出建議

![44444](https://user-images.githubusercontent.com/120545242/209148396-04f9502f-ad12-409a-a0bf-4f895d510fd5.png)

輸入fsm可以得到當下的圖片

![10101010](https://user-images.githubusercontent.com/120545242/209461896-24337dc0-e511-46c9-b2e5-a18099d1a380.png)

輸入開始後即可下一輪的測試

![9999999999999](https://user-images.githubusercontent.com/120545242/209458433-dd7debef-9d89-4dfa-9c72-0c55f290a980.png)



# Line pressuretest
# 目標:做出積分制的壓力測驗
用選項按鈕製作出10題壓力測驗的題目
# 構想:
原本是想做只有選擇的機器人，但後來又想要加入計算分數的系統進去，為了讓返回上一題的分數正確，所以我將不同題目的分數用不同的名詞代替，這樣的話點選上一題那上一題的分數就會歸0
這樣再重新做選擇分數即會正常
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
![fsm](https://user-images.githubusercontent.com/120545242/209146703-6c108b44-5c3e-43ca-9f05-796f9d4bea76.png)
# 使用方式
加入好友後，執行程式，輸入開始即可開始測驗

![螢幕擷取畫面 2022-12-22 214449](https://user-images.githubusercontent.com/120545242/209147414-e178c4da-52e8-4a5f-adc9-bedaddf42ea9.png)

選擇第一題後會跳到第二題，從第二題開始會有返回上一題的選項，點選後會回到上一題再繼續做選擇

![333333](https://user-images.githubusercontent.com/120545242/209147901-2164e0ec-7647-47b2-8348-3d713f63bff4.png)

做完十題後，點選結果，會根據你選擇的選項進行加分最後給出建議

![44444](https://user-images.githubusercontent.com/120545242/209148396-04f9502f-ad12-409a-a0bf-4f895d510fd5.png)

輸入開始後即可下一輪的測試

![5555](https://user-images.githubusercontent.com/120545242/209148582-15c219ec-8fc8-498e-9b3a-5726767ae136.png)


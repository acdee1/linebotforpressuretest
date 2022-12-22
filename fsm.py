from transitions.extensions import GraphMachine
from utils import send_text_message,send_button_message
from linebot.models import MessageTemplateAction
score1=0
score2=0
score3=0
score4=0
score5=0
score6=0
score7=0
score8=0
score9=0
score10=0
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_question1(self, event):
        text = event.message.text
        return text.lower() == '開始' or text.lower() == '返回第一題'
    
    def on_enter_question1(self, event):
        global score1
        if event.message.text.lower()=='返回第一題':
                score1=0
        title = '壓力測驗'
        text = '1.覺得生氣'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='1-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '1-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '1-3'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)
        
    def is_going_to_question2(self, event):
        text = event.message.text
        return text.lower() == '1-1'or text.lower() =='1-2'or text.lower() == '1-3' or text.lower() == '返回第二題'
    
    def on_enter_question2(self, event):
        global score1
        if event.message.text.lower()=='1-1':
                    score1=score1+3
        elif event.message.text.lower()=='1-2':
                    score1=score1+2
        elif event.message.text.lower()=='1-3':
                    score1=score1+1
        global score2
        if event.message.text.lower()=='返回第二題':
                score2=0
        title = '壓力測驗'
        text = '2.感到害怕'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='2-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '2-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '2-3'
            ),
            MessageTemplateAction(
                label = '返回第一題',
                text = '返回第一題'
            ),
            
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question1(self,event):
        text = event.message.text
        return text.lower() == '返回第一題'

    def is_going_to_question3(self, event):
        text = event.message.text
        return text.lower() == '2-1'or text.lower() =='2-2'or text.lower() =='2-3'
    
    def on_enter_question3(self, event):
        global score2
        if event.message.text.lower()=='2-1':
                    score2=score2+3
        elif event.message.text.lower()=='2-2':
                    score2=score2+2
        elif event.message.text.lower()=='2-3':
                    score2=score2+1
        global score3
        if event.message.text.lower()=='返回第三題':
                score3=0
        title = '壓力測驗'
        text = '3.腸胃不適'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='3-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '3-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '3-3'
            ),
            MessageTemplateAction(
                label = '返回第二題',
                text = '返回第二題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question2(self,event):
        text = event.message.text
        return text.lower() == '返回第二題'
    
    def is_going_to_question4(self, event):
        text = event.message.text
        return text.lower() == '3-1'or text.lower() =='3-2'or text.lower() =='3-3'
    
    def on_enter_question4(self, event):
        global score3
        if event.message.text.lower()=='3-1':
                    score3=score3+3
        elif event.message.text.lower()=='3-2':
                    score3=score3+2
        elif event.message.text.lower()=='3-3':
                    score3=score3+1
        global score4
        if event.message.text.lower()=='返回第四題':
                score4=0
        title = '壓力測驗'
        text = '4.頭暈或頭痛'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='4-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '4-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '4-3'
            ),
            MessageTemplateAction(
                label = '返回第三題',
                text = '返回第三題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question3(self,event):
        text = event.message.text
        return text.lower() == '返回第三題'
    
    def is_going_to_question5(self, event):
        text = event.message.text
        return text.lower() == '4-1'or text.lower() =='4-2'or text.lower() =='4-3'
    
    def on_enter_question5(self, event):
        global score4
        if event.message.text.lower()=='4-1':
                    score4=score4+3
        elif event.message.text.lower()=='4-2':
                    score4=score4+2
        elif event.message.text.lower()=='4-3':
                    score4=score4+1
        global score5
        if event.message.text.lower()=='返回第五題':
                score5=0
        title = '壓力測驗'
        text = '5.憂鬱沮喪'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='5-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '5-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '5-3'
            ),
            MessageTemplateAction(
                label = '返回第四題',
                text = '返回第四題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question4(self,event):
        text = event.message.text
        return text.lower() == '返回第四題'
    
    def is_going_to_question6(self, event):
        text = event.message.text
        return text.lower() == '5-1'or text.lower() =='5-2'or text.lower() =='5-3'
    
    def on_enter_question6(self, event):
        global score5
        if event.message.text.lower()=='5-1':
                    score5=score5+3
        elif event.message.text.lower()=='5-2':
                    score5=score5+2
        elif event.message.text.lower()=='5-3':
                    score5=score5+1
        global score6
        if event.message.text.lower()=='返回第六題':
                score6=0
        title = '壓力測驗'
        text = '6.睡不好'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='6-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '6-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '6-3'
            ),
            MessageTemplateAction(
                label = '返回第五題',
                text = '返回第五題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question5(self,event):
        text = event.message.text
        return text.lower() == '返回第五題'
    
    def is_going_to_question7(self, event):
        text = event.message.text
        return text.lower() == '6-1'or text.lower() =='6-2'or text.lower() =='6-3'
    
    def on_enter_question7(self, event):
        global score6
        if event.message.text.lower()=='6-1':
                    score6=score6+3
        elif event.message.text.lower()=='6-2':
                    score6=score6+2
        elif event.message.text.lower()=='6-3':
                    score6=score6+1
        global score7
        if event.message.text.lower()=='返回第七題':
                score7=0
        title = '壓力測驗'
        text = '7.神經質'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='7-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '7-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '7-3'
            ),
            MessageTemplateAction(
                label = '返回第六題',
                text = '返回第六題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question6(self,event):
        text = event.message.text
        return text.lower() == '返回第六題'
    
    def is_going_to_question8(self, event):
        text = event.message.text
        return text.lower() == '7-1'or text.lower() =='7-2'or text.lower() =='7-3'
    
    def on_enter_question8(self, event):
        global score7
        if event.message.text.lower()=='7-1':
                    score7=score7+3
        elif event.message.text.lower()=='7-2':
                    score7=score7+2
        elif event.message.text.lower()=='7-3':
                    score7=score7+1
        global score8
        if event.message.text.lower()=='返回第八題':
                score8=0
        title = '壓力測驗'
        text = '8.緊張焦慮'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='8-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '8-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '8-3'
            ),
            MessageTemplateAction(
                label = '返回第七題',
                text = '返回第七題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question7(self,event):
        text = event.message.text
        return text.lower() == '返回第七題'
    
    def is_going_to_question9(self, event):
        text = event.message.text
        return text.lower() == '8-1'or text.lower() =='8-2'or text.lower() =='8-3'
    
    def on_enter_question9(self, event):
        global score8
        if event.message.text.lower()=='8-1':
                    score8=score8+3
        elif event.message.text.lower()=='8-2':
                    score8=score8+2
        elif event.message.text.lower()=='8-3':
                    score8=score8+1
        global score9
        if event.message.text.lower()=='返回第九題':
                score9=0
        title = '壓力測驗'
        text = '9.覺得崩潰'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='9-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '9-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '9-3'
            ),
            MessageTemplateAction(
                label = '返回第八題',
                text = '返回第八題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question8(self,event):
        text = event.message.text
        return text.lower() == '返回第八題'
    
    def is_going_to_question10(self, event):
        text = event.message.text
        return text.lower() == '9-1'or text.lower() =='9-2'or text.lower() =='9-3'
    
    def on_enter_question10(self, event):
        global score9
        if event.message.text.lower()=='9-1':
                    score9=score9+3
        elif event.message.text.lower()=='9-2':
                    score9=score9+2
        elif event.message.text.lower()=='9-3':
                    score9=score9+1
        title = '壓力測驗'
        text = '10.財務負擔重'
        btn = [
            MessageTemplateAction(
                label = '總是',
                text ='10-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '10-2'
            ),
            MessageTemplateAction(
                label = '從不',
                text = '10-3'
            ),
            MessageTemplateAction(
                label = '返回第九題',
                text = '返回第九題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_question9(self,event):
        text = event.message.text
        return text.lower() == '返回第九題'
    
    def is_going_to_result(self, event):
        text = event.message.text
        return text.lower() == '10-1'or text.lower() =='10-2'or text.lower() =='10-3'
    
    def on_enter_result(self, event):
        global score10
        if event.message.text.lower()=='10-1':
                    score10=score10+3
        elif event.message.text.lower()=='10-2':
                    score10=score10+2
        elif event.message.text.lower()=='10-3':
                    score10=score10+1
        title = '壓力測驗'
        text = '結果'
        btn = [
            MessageTemplateAction(
                label = '結果',
                text ='結果'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def is_going_to_user(self,event):
        text = event.message.text
        return text.lower() == '結果'
    
    def on_enter_user(self,event): 
        global score1
        global score2
        global score3
        global score4
        global score5
        global score6
        global score7
        global score8
        global score9
        global score10
        if score1+score2+score3+score4+score5+score6+score7+score8+score9+score10<=30 and score1+score2+score3+score4+score5+score6+score7+score8+score9+score10>23:
               send_text_message(event.reply_token, "您的壓力太大，有時候需要冷靜下來現在的自己需要的是甚麼，需要去觀察如何讓自己解決困難,請輸入開始開啟下一次測驗")
        elif score1+score2+score3+score4+score5+score6+score7+score8+score9+score10<=23 and score1+score2+score3+score4+score5+score6+score7+score8+score9+score10>16:
               send_text_message(event.reply_token, '您的壓力偏大，多多跟自己認識的朋友聊天，從聊天出發去紓壓自己的壓力,請輸入開始開啟下一次測驗')
        elif score1+score2+score3+score4+score5+score6+score7+score8+score9+score10<=16 and score1+score2+score3+score4+score5+score6+score7+score8+score9+score10>=10:
               send_text_message(event.reply_token, "您的近期壓力有點高，建議多多去做自己的愛好去抒發累積的壓力,請輸入開始開啟下一次測驗")
        score1=0
        score2=0
        score3=0
        score4=0
        score5=0
        score6=0
        score7=0
        score8=0
        score9=0
        score10=0
      
    
    
 
   

         
    


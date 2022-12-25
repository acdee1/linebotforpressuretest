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
familyscore1=0
familyscore2=0
familyscore3=0
familyscore4=0
familyscore5=0
familyscore6=0
familyscore7=0
familyscore8=0
familyscore9=0
familyscore10=0
workscore1=0
workscore2=0
workscore3=0
workscore4=0
workscore5=0
workscore6=0
workscore7=0
workscore8=0
workscore9=0
workscore10=0
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_test(self,event):
        text=event.message.text
        return text.lower()=='開始'
    
    def on_enter_test(self,event):
        title = '壓力測驗'
        text = '選擇壓力測驗種類'
        btn = [
            MessageTemplateAction(
                label = '工作壓力測驗',
                text ='工作壓力測驗'
            ),
            MessageTemplateAction(
                label = '家庭壓力測驗',
                text = '家庭壓力測驗'
            ),
            MessageTemplateAction(
                label = '綜合壓力測驗',
                text = '綜合壓力測驗'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)
#綜合壓力測驗
    def is_going_to_question1(self, event):
        text = event.message.text
        return text.lower() == '返回第一題' or text.lower()=='綜合壓力測驗'
    
    def on_enter_question1(self, event):
        global score1
        if event.message.text.lower()=='返回第一題':
                score1=0
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
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
        title = '綜合壓力測驗'
        text = '結果'
        btn = [
            MessageTemplateAction(
                label = '結果',
                text ='結果'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

#家庭壓力測驗
    def is_going_to_familyquestion1(self, event):
        text = event.message.text
        return text.lower() == '返回第一題' or text.lower()=='家庭壓力測驗'
    
    def on_enter_familyquestion1(self, event):
        global familyscore1
        if event.message.text.lower()=='返回第一題':
                familyscore1=0
        title = '家庭壓力測驗'
        text = '跟父母相處的態度'
        btn = [
            MessageTemplateAction(
                label = '態度不佳',
                text ='1-1'
            ),
            MessageTemplateAction(
                label = '平凡無奇',
                text = '1-2'
            ),
            MessageTemplateAction(
                label = '態度良好',
                text = '1-3'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)
        
    def is_going_to_familyquestion2(self, event):
        text = event.message.text
        return text.lower() == '1-1'or text.lower() =='1-2'or text.lower() == '1-3' or text.lower() == '返回第二題'
    
    def on_enter_familyquestion2(self, event):
        global familyscore1
        if event.message.text.lower()=='1-1':
                    familyscore1=familyscore1+3
        elif event.message.text.lower()=='1-2':
                    familyscore1=familyscore1+2
        elif event.message.text.lower()=='1-3':
                    familyscore1=familyscore1+1
        global familyscore2
        if event.message.text.lower()=='返回第二題':
                familyscore2=0
        title = '家庭壓力測驗'
        text = '時常跟父母吵架'
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

    def back_to_familyquestion1(self,event):
        text = event.message.text
        return text.lower() == '返回第一題'

    def is_going_to_familyquestion3(self, event):
        text = event.message.text
        return text.lower() == '2-1'or text.lower() =='2-2'or text.lower() =='2-3'
    
    def on_enter_familyquestion3(self, event):
        global familyscore2
        if event.message.text.lower()=='2-1':
                    familyscore2=familyscore2+3
        elif event.message.text.lower()=='2-2':
                    familyscore2=familyscore2+2
        elif event.message.text.lower()=='2-3':
                    familyscore2=familyscore2+1
        global familyscore3
        if event.message.text.lower()=='返回第三題':
                familyscore3=0
        title = '家庭壓力測驗'
        text = '跟兄弟姊妹相處'
        btn = [
            MessageTemplateAction(
                label = '相處差',
                text ='3-1'
            ),
            MessageTemplateAction(
                label = '互不干擾',
                text = '3-2'
            ),
            MessageTemplateAction(
                label = '每天都很愉快',
                text = '3-3'
            ),
            MessageTemplateAction(
                label = '返回第二題',
                text = '返回第二題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_familyquestion2(self,event):
        text = event.message.text
        return text.lower() == '返回第二題'
    
    def is_going_to_familyquestion4(self, event):
        text = event.message.text
        return text.lower() == '3-1'or text.lower() =='3-2'or text.lower() =='3-3'
    
    def on_enter_familyquestion4(self, event):
        global familyscore3
        if event.message.text.lower()=='3-1':
                    familyscore3=familyscore3+3
        elif event.message.text.lower()=='3-2':
                    familyscore3=familyscore3+2
        elif event.message.text.lower()=='3-3':
                    familyscore3=familyscore3+1
        global familyscore4
        if event.message.text.lower()=='返回第四題':
                familyscore4=0
        title = '家庭壓力測驗'
        text = '常常跟家人出去玩嗎'
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

    def back_to_familyquestion3(self,event):
        text = event.message.text
        return text.lower() == '返回第三題'
    
    def is_going_to_familyquestion5(self, event):
        text = event.message.text
        return text.lower() == '4-1'or text.lower() =='4-2'or text.lower() =='4-3'
    
    def on_enter_familyquestion5(self, event):
        global familyscore4
        if event.message.text.lower()=='4-1':
                    familyscore4=familyscore4+3
        elif event.message.text.lower()=='4-2':
                    familyscore4=familyscore4+2
        elif event.message.text.lower()=='4-3':
                    familyscore4=familyscore4+1
        global familyscore5
        if event.message.text.lower()=='返回第五題':
                familyscore5=0
        title = '家庭壓力測驗'
        text = '有時常跟家人聯絡嗎'
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

    def back_to_familyquestion4(self,event):
        text = event.message.text
        return text.lower() == '返回第四題'
    
    def is_going_to_familyquestion6(self, event):
        text = event.message.text
        return text.lower() == '5-1'or text.lower() =='5-2'or text.lower() =='5-3'
    
    def on_enter_familyquestion6(self, event):
        global familyscore5
        if event.message.text.lower()=='5-1':
                    familyscore5=familyscore5+3
        elif event.message.text.lower()=='5-2':
                    familyscore5=familyscore5+2
        elif event.message.text.lower()=='5-3':
                    familyscore5=familyscore5+1
        global familyscore6
        if event.message.text.lower()=='返回第六題':
                familyscore6=0
        title = '家庭壓力測驗'
        text = '做什麼事都會報備嗎'
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

    def back_to_familyquestion5(self,event):
        text = event.message.text
        return text.lower() == '返回第五題'
    
    def is_going_to_familyquestion7(self, event):
        text = event.message.text
        return text.lower() == '6-1'or text.lower() =='6-2'or text.lower() =='6-3'
    
    def on_enter_familyquestion7(self, event):
        global familyscore6
        if event.message.text.lower()=='6-1':
                    familyscore6=familyscore6+3
        elif event.message.text.lower()=='6-2':
                    familyscore6=familyscore6+2
        elif event.message.text.lower()=='6-3':
                    familyscore6=familyscore6+1
        global familyscore7
        if event.message.text.lower()=='返回第七題':
                familyscore7=0
        title = '家庭壓力測驗'
        text = '父母有花時間陪伴你嗎'
        btn = [
            MessageTemplateAction(
                label = '從不',
                text ='7-1'
            ),
            MessageTemplateAction(
                label = '偶爾',
                text = '7-2'
            ),
            MessageTemplateAction(
                label = '總是',
                text = '7-3'
            ),
            MessageTemplateAction(
                label = '返回第六題',
                text = '返回第六題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_familyquestion6(self,event):
        text = event.message.text
        return text.lower() == '返回第六題'
    
    def is_going_to_familyquestion8(self, event):
        text = event.message.text
        return text.lower() == '7-1'or text.lower() =='7-2'or text.lower() =='7-3'
    
    def on_enter_familyquestion8(self, event):
        global familyscore7
        if event.message.text.lower()=='7-1':
                    familyscore7=familyscore7+3
        elif event.message.text.lower()=='7-2':
                    familyscore7=familyscore7+2
        elif event.message.text.lower()=='7-3':
                    familyscore7=familyscore7+1
        global familyscore8
        if event.message.text.lower()=='返回第八題':
                familyscore8=0
        title = '家庭壓力測驗'
        text = '一年內跟家人住的時間'
        btn = [
            MessageTemplateAction(
                label = '整年',
                text ='8-1'
            ),
            MessageTemplateAction(
                label = '半年',
                text = '8-2'
            ),
            MessageTemplateAction(
                label = '幾乎沒有',
                text = '8-3'
            ),
            MessageTemplateAction(
                label = '返回第七題',
                text = '返回第七題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_familyquestion7(self,event):
        text = event.message.text
        return text.lower() == '返回第七題'
    
    def is_going_to_familyquestion9(self, event):
        text = event.message.text
        return text.lower() == '8-1'or text.lower() =='8-2'or text.lower() =='8-3'
    
    def on_enter_familyquestion9(self, event):
        global familyscore8
        if event.message.text.lower()=='8-1':
                    familyscore8=familyscore8+3
        elif event.message.text.lower()=='8-2':
                    familyscore8=familyscore8+2
        elif event.message.text.lower()=='8-3':
                    familyscore8=familyscore8+1
        global familyscore9
        if event.message.text.lower()=='返回第九題':
                familyscore9=0
        title = '家庭壓力測驗'
        text = '父母常常會嘮叨'
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

    def back_to_familyquestion8(self,event):
        text = event.message.text
        return text.lower() == '返回第八題'
    
    def is_going_to_familyquestion10(self, event):
        text = event.message.text
        return text.lower() == '9-1'or text.lower() =='9-2'or text.lower() =='9-3'
    
    def on_enter_familyquestion10(self, event):
        global familyscore9
        if event.message.text.lower()=='9-1':
                    familyscore9=familyscore9+3
        elif event.message.text.lower()=='9-2':
                    familyscore9=familyscore9+2
        elif event.message.text.lower()=='9-3':
                    familyscore9=familyscore9+1
        title = '家庭壓力測驗'
        text = '是否想盡快離開家'
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

    def back_to_familyquestion9(self,event):
        text = event.message.text
        return text.lower() == '返回第九題'
    
    def is_going_to_familyresult(self, event):
        text = event.message.text
        return text.lower() == '10-1'or text.lower() =='10-2'or text.lower() =='10-3'
    
    def on_enter_familyresult(self, event):
        global familyscore10
        if event.message.text.lower()=='10-1':
                    familyscore10=familyscore10+3
        elif event.message.text.lower()=='10-2':
                    familyscore10=familyscore10+2
        elif event.message.text.lower()=='10-3':
                    familyscore10=familyscore10+1
        title = '家庭壓力測驗'
        text = '結果'
        btn = [
            MessageTemplateAction(
                label = '結果',
                text ='結果'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)
   
      
#工作壓力測驗


    def is_going_to_workquestion1(self,event):
        text = event.message.text
        return text.lower() == '返回第一題' or text.lower()=='工作壓力測驗'
    
    def on_enter_workquestion1(self, event):
        global workscore1
        if event.message.text.lower()=='返回第一題':
                workscore1=0
        title = '工作壓力測驗'
        text = '1.如何管理上班時間'
        btn = [
            MessageTemplateAction(
                label = '工作上對時間沒有太多掌控',
                text ='1-1'
            ),
            MessageTemplateAction(
                label = '可決定部分時間但還是希望有更多時間掌控',
                text = '1-2'
            ),
            MessageTemplateAction(
                label = '我可以有彈性時間利用時間去休息',
                text = '1-3'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)
        
    def is_going_to_workquestion2(self, event):
        text = event.message.text
        return text.lower() == '1-1'or text.lower() =='1-2'or text.lower() == '1-3' or text.lower() == '返回第二題'
    
    def on_enter_workquestion2(self, event):
        global workscore1
        if event.message.text.lower()=='1-1':
                    workscore1=workscore1+3
        elif event.message.text.lower()=='1-2':
                    workscore1=workscore1+2
        elif event.message.text.lower()=='1-3':
                    workscore1=workscore1+1
        global workscore2
        if event.message.text.lower()=='返回第二題':
                workscore2=0
        title = '工作壓力測驗'
        text = '2.感到害怕'
        btn = [
            MessageTemplateAction(
                label = '當工作內容改變時,你可以做什麼',
                text ='我不會被告知要改變且不會跟老闆討論到'
            ),
            MessageTemplateAction(
                label = '會被提前告知但沒辦法做出決策',
                text = '2-2'
            ),
            MessageTemplateAction(
                label = '我有機會跟老闆討論工作上的改變',
                text = '2-3'
            ),
            MessageTemplateAction(
                label = '返回第一題',
                text = '返回第一題'
            ),
            
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion1(self,event):
        text = event.message.text
        return text.lower() == '返回第一題'

    def is_going_to_workquestion3(self, event):
        text = event.message.text
        return text.lower() == '2-1'or text.lower() =='2-2'or text.lower() =='2-3'
    
    def on_enter_workquestion3(self, event):
        global workscore2
        if event.message.text.lower()=='2-1':
                    workscore2=workscore2+3
        elif event.message.text.lower()=='2-2':
                    workscore2=workscore2+2
        elif event.message.text.lower()=='2-3':
                    workscore2=workscore2+1
        global workscore3
        if event.message.text.lower()=='返回第三題':
                workscore3=0
        title = '工作壓力測驗'
        text = '和同事相處得如何'
        btn = [
            MessageTemplateAction(
                label = '相處得很差幾乎沒有交集',
                text ='3-1'
            ),
            MessageTemplateAction(
                label = '偶爾會約出去吃飯',
                text = '3-2'
            ),
            MessageTemplateAction(
                label = '每天都會有交集且合作得很好',
                text = '3-3'
            ),
            MessageTemplateAction(
                label = '返回第二題',
                text = '返回第二題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion2(self,event):
        text = event.message.text
        return text.lower() == '返回第二題'
    
    def is_going_to_workquestion4(self, event):
        text = event.message.text
        return text.lower() == '3-1'or text.lower() =='3-2'or text.lower() =='3-3'
    
    def on_enter_workquestion4(self, event):
        global workscore3
        if event.message.text.lower()=='3-1':
                    workscore3=workscore3+3
        elif event.message.text.lower()=='3-2':
                    workscore3=workscore3+2
        elif event.message.text.lower()=='3-3':
                    workscore3=workscore3+1
        global workscore4
        if event.message.text.lower()=='返回第四題':
                workcore4=0
        title = '工作壓力測驗'
        text = '哪一項最符合你對自己工作角色的看法'
        btn = [
            MessageTemplateAction(
                label = '我不清楚我的工作角色',
                text ='4-1'
            ),
            MessageTemplateAction(
                label = '我理解職責,但沒辦法完成工作',
                text = '4-2'
            ),
            MessageTemplateAction(
                label = '清楚了解工作角色且能完成所有的職責',
                text = '4-3'
            ),
            MessageTemplateAction(
                label = '返回第三題',
                text = '返回第三題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion3(self,event):
        text = event.message.text
        return text.lower() == '返回第三題'
    
    def is_going_to_workquestion5(self, event):
        text = event.message.text
        return text.lower() == '4-1'or text.lower() =='4-2'or text.lower() =='4-3'
    
    def on_enter_workquestion5(self, event):
        global workscore4
        if event.message.text.lower()=='4-1':
                    workscore4=workscore4+3
        elif event.message.text.lower()=='4-2':
                    workscore4=workscore4+2
        elif event.message.text.lower()=='4-3':
                    workscore4=workscore4+1
        global workscore5
        if event.message.text.lower()=='返回第五題':
                workscore5=0
        title = '工作壓力測驗'
        text = '和老闆相處如何'
        btn = [
            MessageTemplateAction(
                label = '相處得不好也得不到幫助',
                text ='5-1'
            ),
            MessageTemplateAction(
                label = '我能和老闆在工作討論問題僅此而已',
                text = '5-2'
            ),
            MessageTemplateAction(
                label = '我相信老闆能給我協助',
                text = '5-3'
            ),
            MessageTemplateAction(
                label = '返回第四題',
                text = '返回第四題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion4(self,event):
        text = event.message.text
        return text.lower() == '返回第四題'
    
    def is_going_to_workquestion6(self, event):
        text = event.message.text
        return text.lower() == '5-1'or text.lower() =='5-2'or text.lower() =='5-3'
    
    def on_enter_workquestion6(self, event):
        global workscore5
        if event.message.text.lower()=='5-1':
                    workscore5=workscore5+3
        elif event.message.text.lower()=='5-2':
                    workscore5=workscore5+2
        elif event.message.text.lower()=='5-3':
                    workscore5=workscore5+1
        global workscore6
        if event.message.text.lower()=='返回第六題':
                workscore6=0
        title = '工作壓力測驗'
        text = '對於工作的完成度'
        btn = [
            MessageTemplateAction(
                label = '幾乎沒有',
                text ='6-1'
            ),
            MessageTemplateAction(
                label = '一半',
                text = '6-2'
            ),
            MessageTemplateAction(
                label = '能夠準時完成',
                text = '6-3'
            ),
            MessageTemplateAction(
                label = '返回第五題',
                text = '返回第五題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion5(self,event):
        text = event.message.text
        return text.lower() == '返回第五題'
    
    def is_going_to_workquestion7(self, event):
        text = event.message.text
        return text.lower() == '6-1'or text.lower() =='6-2'or text.lower() =='6-3'
    
    def on_enter_workquestion7(self, event):
        global workscore6
        if event.message.text.lower()=='6-1':
                    workscore6=workscore6+3
        elif event.message.text.lower()=='6-2':
                    workscore6=workscore6+2
        elif event.message.text.lower()=='6-3':
                    workscore6=workscore6+1
        global workscore7
        if event.message.text.lower()=='返回第七題':
                workscore7=0
        title = '工作壓力測驗'
        text = '需要時常加班嗎'
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

    def back_to_workquestion6(self,event):
        text = event.message.text
        return text.lower() == '返回第六題'
    
    def is_going_to_workquestion8(self, event):
        text = event.message.text
        return text.lower() == '7-1'or text.lower() =='7-2'or text.lower() =='7-3'
    
    def on_enter_workquestion8(self, event):
        global workscore7
        if event.message.text.lower()=='7-1':
                    workscore7=workscore7+3
        elif event.message.text.lower()=='7-2':
                    workscore7=workscore7+2
        elif event.message.text.lower()=='7-3':
                    workscore7=workscore7+1
        global workscore8
        if event.message.text.lower()=='返回第八題':
                workscore8=0
        title = '工作壓力測驗'
        text = '對於目前工作的滿意程度'
        btn = [
            MessageTemplateAction(
                label = '不滿意',
                text ='8-1'
            ),
            MessageTemplateAction(
                label = '還好',
                text = '8-2'
            ),
            MessageTemplateAction(
                label = '很滿意',
                text = '8-3'
            ),
            MessageTemplateAction(
                label = '返回第七題',
                text = '返回第七題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion7(self,event):
        text = event.message.text
        return text.lower() == '返回第七題'
    
    def is_going_to_workquestion9(self, event):
        text = event.message.text
        return text.lower() == '8-1'or text.lower() =='8-2'or text.lower() =='8-3'
    
    def on_enter_workquestion9(self, event):
        global workscore8
        if event.message.text.lower()=='8-1':
                    workscore8=workscore8+3
        elif event.message.text.lower()=='8-2':
                    workscore8=workscore8+2
        elif event.message.text.lower()=='8-3':
                    workscore8=workscore8+1
        global workscore9
        if event.message.text.lower()=='返回第九題':
                workscore9=0
        title = '工作壓力測驗'
        text = '工作量'
        btn = [
            MessageTemplateAction(
                label = '高到難以負荷',
                text ='9-1'
            ),
            MessageTemplateAction(
                label = '還好',
                text = '9-2'
            ),
            MessageTemplateAction(
                label = '輕鬆',
                text = '9-3'
            ),
            MessageTemplateAction(
                label = '返回第八題',
                text = '返回第八題'
            )
        ]
        send_button_message(event.reply_token, title, text, btn)

    def back_to_workquestion8(self,event):
        text = event.message.text
        return text.lower() == '返回第八題'
    
    def is_going_to_workquestion10(self, event):
        text = event.message.text
        return text.lower() == '9-1'or text.lower() =='9-2'or text.lower() =='9-3'
    
    def on_enter_workquestion10(self, event):
        global workscore9
        if event.message.text.lower()=='9-1':
                    workscore9=workscore9+3
        elif event.message.text.lower()=='9-2':
                    workscore9=workscore9+2
        elif event.message.text.lower()=='9-3':
                    workscore9=workscore9+1
        title = '工作壓力測驗'
        text = '老闆對待員工不公'
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

    def back_to_workquestion9(self,event):
        text = event.message.text
        return text.lower() == '返回第九題'
    
    def is_going_to_workresult(self, event):
        text = event.message.text
        return text.lower() == '10-1'or text.lower() =='10-2'or text.lower() =='10-3'
    
    def on_enter_workresult(self, event):
        global workscore10
        if event.message.text.lower()=='10-1':
                    workscore10=workscore10+3
        elif event.message.text.lower()=='10-2':
                    workscore10=workscore10+2
        elif event.message.text.lower()=='10-3':
                    workscore10=workscore10+1
        title = '工作壓力測驗'
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
        global familyscore1
        global familyscore2
        global familyscore3
        global familyscore4
        global familyscore5
        global familyscore6
        global familyscore7
        global familyscore8
        global familyscore9
        global familyscore10
        if familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10<=30 and familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10>23:
               send_text_message(event.reply_token, "您的家庭壓力太大，需要找時間坐下來跟家庭溝通表達你需要什麼，請輸入開始開啟下一次測驗")
        elif familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10<=23 and familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10>16:
               send_text_message(event.reply_token, '您的家庭壓力偏大，父母雖然會嘮叨但都是為了你想所以有時候需要去好好聽他們所說的，請輸入開始開啟下一次測驗')
        elif familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10<=16 and familyscore1+familyscore2+familyscore3+familyscore4+familyscore5+familyscore6+familyscore7+familyscore8+familyscore9+familyscore10>=10:
               send_text_message(event.reply_token, "您的家庭壓力機會沒有，建議多多去做自己的愛好去抒發累積的壓力，請輸入開始開啟下一次測驗")
        familyscore1=0
        familyscore2=0
        familyscore3=0
        familyscore4=0
        familyscore5=0
        familyscore6=0
        familyscore7=0
        familyscore8=0
        familyscore9=0
        familyscore10=0
        
        global workscore1
        global workscore2
        global workscore3
        global workscore4
        global workscore5
        global workscore6
        global workscore7
        global workscore8
        global workscore9
        global workscore10
        if workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10<=30 and workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10>23:
               send_text_message(event.reply_token, "您的工作壓力太大，工作給你的壓力太大，或許需要思考轉跑道或者從根本了解問題，請輸入開始開啟下一次測驗")
        elif workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10<=23 and workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10>16:
               send_text_message(event.reply_token, '您的工作壓力偏大，多多跟老闆跟同事溝通用雙向的溝通去解決問題，請輸入開始開啟下一次測驗')
        elif workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10<=16 and workscore1+workscore2+workscore3+workscore4+workscore5+workscore6+workscore7+workscore8+workscore9+workscore10>=10:
               send_text_message(event.reply_token, "您的工作壓力有點低，你跟同事還有老闆的相處很好，請輸入開始開啟下一次測驗")
        workscore1=0
        workscore2=0
        workscore3=0
        workscore4=0
        workscore5=0
        workscore6=0
        workscore7=0
        workscore8=0
        workscore9=0
        workscore10=0   
    
 
   

         
    


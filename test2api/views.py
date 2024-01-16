from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, PostbackEvent
from urllib.parse import parse_qsl
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if event.message.type == 'image':
                    func.imagereply(event)
                else:
                    mtext = str(event.message.text)
                    
                    if mtext == 'Reminder Switch':
                        func.switchon(event)
                        
                    elif mtext == 'Close Reminder':
                        func.switchoff(event)
                        
                    elif mtext == 'Reminder?' or mtext == 'Reminder？':
                        func.reminders(event)
                    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
                    elif mtext[0] == '#':
                        func.getreminder(event)
                    
                    elif mtext[0:2] == 'Edit':
                        try:
                            a=mtext[2]
                            func.edit(event)
                        except:
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Please enter\n\'Edit[TaskName]\'\nFor example:Edit Being handsome'))
                            
                    elif mtext[0:2] == 'Delete':
                        try:
                            a=mtext[2] #檢查後面有沒有東西
                            func.delete(event)
                        except:
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Please enter\n\'Delete[TaskName]\'\nFor example:\Delete Being handsome'))
                        
                    elif mtext=='ShowAllReminders':
                        func.checkreminder(event)
                   
                    elif mtext[0:6]=='Lucky;' or mtext[0:6]=='lucky;' or mtext[0:6]=='Lucky；' or mtext[0:6]=='lucky；':
                        func.learn(event)
                    
                    elif mtext[0:3]=='拉奇;'or mtext[0:3]=='拉奇；':
                        func.learn2(event)    
                        
                    elif mtext[0:8]=='LuckyForget;' or mtext[0:8]=='luckyForget;' or mtext[0:8]=='luckyForget；' or mtext[0:8]=='luckyForget；':
                        func.forget(event)
                        
                    elif mtext[0:5]=='拉奇忘記;'or mtext[0:5]=='拉奇忘記；':
                        func.forget2(event)
                   
                    elif mtext=='luckyTalk' or mtext=='LuckyTalk' or mtext=='拉奇你會說什麼':
                        func.checktalk(event)
                        
                    elif mtext[:2] == '+$':
                        func.editmoney(event)
                    
                    elif mtext[:2] == '-$':
                        func.deletemoney(event)
                    
                    elif mtext[:3] == '$MySpending':
                        try:
                            a=mtext[4]
                            func.checkmoney(event)
                        except:
                            func.checkexample(event)
                    
                    elif mtext == '$?' or mtext == '$？':
                        func.example(event)    
                    
                    elif mtext[0] == '$' and len(mtext)>1:
                        func.getmoney(event)
                        
                    elif mtext=='lucky' or mtext=='Lucky' or mtext=='拉奇':
                        func.allexamples(event)
                    
                        
                    else :
                        func.reply(event)
            if isinstance(event,PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data)) #取得postback資料
                if backdata.get('action')== 'add':
                    func.addreminder(event, backdata)
                                        
                elif backdata.get('action')== 'time':
                    func.gettime(event, backdata)
                    
                elif backdata.get('action')== 'notime':
                    func.notime(event, backdata) 
                    
                elif backdata.get('action')=='sell':
                    func.sendtime(event, backdata)
                    
                elif backdata.get('action')== 'edit':
                    func.editreminder(event, backdata)
                    
                elif backdata.get('action')=='selledit':
                    func.edittime(event, backdata)
                    
                elif backdata.get('action')=='delete':
                    func.deletereminder(event, backdata)
                    
                elif backdata.get('action')=='yesdelete':
                    func.yesdelete(event, backdata)
                    
                elif backdata.get('action')=='nodelete':
                    func.nodelete(event, backdata)
                    
                elif backdata.get('action')=='food':
                    func.food(event, backdata)
                    
                elif backdata.get('action')=='trans':
                    func.trans(event, backdata)
                    
                elif backdata.get('action')=='daily':
                    func.daily(event, backdata)
                    
                elif backdata.get('action')=='entertainment':
                    func.entertainment(event, backdata)
                    
                elif backdata.get('action')=='cloth':
                    func.cloth(event, backdata)
                    
                elif backdata.get('action')=='medical':
                    func.medical(event, backdata)
                    
                elif backdata.get('action')=='other':
                    func.other(event, backdata)
                
                elif backdata.get('action')=='forget':
                    func.forgetmoney(event, backdata)
                
                elif backdata.get('action')=='delete$':
                    func.deleteexample(event, backdata)
                    
                elif backdata.get('action')=='1':
                    func.moneytime(event, backdata)
                
                elif backdata.get('action')=='2':
                    func.deletemoneytime(event, backdata)
                
                elif backdata.get('action')=='3':
                    func.checkexample(event)
                
                elif backdata.get('action')=='today':
                    func.today(event, backdata)
                    
                elif backdata.get('action')=='yesterday':
                    func.yesterday(event, backdata)  
                    
                elif backdata.get('action')=='thismonth':
                    func.thismonth(event, backdata)
                    
                elif backdata.get('action')=='lastmonth':
                    func.lastmonth(event, backdata)
                    
                elif backdata.get('action')=='thisyear':
                    func.thisyear(event, backdata)
                
                elif backdata.get('action')=='lastyear':
                    func.lastyear(event, backdata)
                    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

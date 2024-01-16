from django.conf import settings
from linebot import LineBotApi
from linebot.models import DatetimePickerAction, DatetimePickerTemplateAction, ConfirmTemplate,PostbackAction,TextSendMessage, MessageAction,TemplateSendMessage,ButtonsTemplate, MessageTemplateAction,PostbackTemplateAction
from test2api.models import reminder
import time
import datetime
import schedule
import threading

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
       
def job(event):
    try:
#        to = event.source.user_id
#        line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
        print(123)
        schedule.every(1).seconds.do(job,event)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Error'))
    # create a thread
        a = threading.Thread(target = job(event))
    
    # start a thread
        a.start()
while True:
    schedule.run_pending()
    time.sleep(1)
    
        
    
    #    user_id = event.source.user_id
    #    print(user_id)
    #    line_bot_api.push_message(user_id,TextSendMessage(text='Hello World!'))
    #    schedule.every(1).seconds.do(job,event)    
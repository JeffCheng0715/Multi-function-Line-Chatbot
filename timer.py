from django.conf import settings
from linebot import LineBotApi
from linebot.models import StickerSendMessage,QuickReply, QuickReplyButton, DatetimePickerAction, DatetimePickerTemplateAction, ConfirmTemplate,PostbackAction,TextSendMessage, MessageAction,TemplateSendMessage,ButtonsTemplate, MessageTemplateAction,PostbackTemplateAction
import datetime
from threading import Timer
import pytz
import random
tw = pytz.timezone('Asia/Taipei')
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linebotTest2.settings") #pjname請改為你的專案目錄名稱
django.setup() 

from test2api.models import reminder
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# try:
    
#       target=reminder.objects.all().filter(cTime=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'))
target=reminder.objects.all().exclude(cTime=None).order_by('cTime')[:1]
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
print(str(target[0].cTime)[:-3])
# global nTimer
# # 子執行緒的工作函數    
# nTimer = Timer(10, job)
if target.count() == 0:
    print("null")
else:
    if str(target[0].cTime)[:-3] == datetime.datetime.now().strftime('%Y-%m-%d %H:%M'):
        a=['今日事今日畢','別偷懶了','嗷~~~','白天工作 晚上讀書 假日批判！']
        random.shuffle(a)
        message=[TextSendMessage(
                text=a[0]+'\n時間到囉\n快點\'{}\''.format(str(target[0].cName))
                ),
            StickerSendMessage(package_id=11539,sticker_id=52114117)
            ]
        line_bot_api.push_message(target[0].cid,message)
        target[0].delete()
#     nTimer.cancel()
# if str(target)[11]==']':
#     nTimer.cancel()
#     print('timer stop')
#     return

# if s.num == 0:
#     nTimer.cancel()
# else:
#     nTimer.start()
#        to = event.source.user_id
#        line_bot_api.push_message(to,TextSendMessage(text='Hello World!'))
# except:
#     target=reminder.objects.all().exclude(cTime=None).order_by('cTime')[:1]
#     line_bot_api.push_message(target[0].cid,TextSendMessage(text='提醒發生問題'))
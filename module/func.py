from django.conf import settings
from linebot import LineBotApi
from linebot.models import StickerSendMessage,QuickReply, QuickReplyButton, DatetimePickerAction, DatetimePickerTemplateAction, ConfirmTemplate,PostbackAction,TextSendMessage, MessageAction,TemplateSendMessage,ButtonsTemplate, MessageTemplateAction,PostbackTemplateAction
from test2api.models import reminder, talk, money, switch
import datetime
from threading import Timer
import pytz
import random
tw = pytz.timezone('Asia/Taipei')

#global to

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
def allexamples(event):
    message = [TextSendMessage(text='Hi there, My name is Lucky\nI am your personal assistant chatbot.\nLet us see what can I do!'),
               TextSendMessage(text='First of all\n-----------Reminder------------\n'
                               +'Type Reminder? \tfor more info about reminder\n\n'
                               +'Type #[TaskName]\tto add a task\nFor example:#Dating with my crush\n\n'
                               +'Type edit[TaskName]:\tif you want to change something\nFor example:edit Dating with my crush\n\n'
                               +'Type ShowAllReminders:\tI will show you all active reminders'),
               TextSendMessage(text='Secondly\n-----------Track Your Spending------------\n'
                               +'Type $[Price]:\tto add an expense. And then an category selecting menu will pop up.\n\n'
                               +'Type $[Price]/[Category]:\tto add a category in the default menu\n\n'
                               +'Type +$[Price]/[Category]:\tto add a spending in the past.The time selecting menu will pop up\n\n'
                               +'Type -$[Price]/[Category]:\tto delete a spending record.\n\n'
                               +'Type $MySpending:\tto show all the spending you had~\n'
                               +'For more detail, you can add Year(YYYY),Month(YYYY/MM)\nor Day(YYYY/MM/DD)\nFor example:$MySpending2019/5/6\n\n'
                               +'Type $?:\tfor more info'),
               TextSendMessage(text='Last but not least\n\n----------Chating-----------\n'
                               +'Type Lucky;[What you want to say to Lucky];[What Lucky will response] or\n拉奇;[What you want to say to Lucky];[What Lucky will response]\n For example: Lucky;1+1;equals 2!\n\n'
                               +'Type LuckyForget;[What you want to say to Lucky] or\t拉奇忘記;[What you want to say to Lucky]\tI will not respond to this keyword anymore\n\n'
                               +'Type LuckyTalk or\n拉奇你會說甚麼\t I will show you everything I learned\n\n'
                               +'I will randomly respond if I cannot understand\n\n'
                               +'That will be it! If you forget any command. Just call my name: Lucky\n'
                               +'I will be there anytime.'),
               StickerSendMessage(package_id=11539,sticker_id=52114118)]
                               
              
    line_bot_api.reply_message(event.reply_token,message)

   
def reply(event):    

    try:
    
        if talk.objects.filter(cget=event.message.text).count() > 0 :
            obj = talk.objects.get(cget=event.message.text)
            if obj.csay.find('/') == -1:
                message = TextSendMessage(
                        text=obj.csay
                        )
                line_bot_api.reply_message(event.reply_token,message)
            else:
                a=[]
                text=obj.csay
                indices = [i for i, x in enumerate(text) if x == "/"]
                for i in range(len(indices)+1):
                    index=text.find("/")
                    if i==len(indices):
                        a.append(text)
                    else:
                        a.append(text[:index])
                    text=text[index+1:]
                random.shuffle(a)
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a[0]))
                
        else:
            a=[11537,11538,11539]
            random.shuffle(a) 
            if a[0] == 11537:
                b = list(range(52002734, 52002773))
                random.shuffle(b) 
            elif a[0] == 11538:
                b = list(range(51626494, 51626533))
                random.shuffle(b) 
            else:
                a[0] = 11539
                b = list(range(52114110, 52114149))
                random.shuffle(b) 
    
            message = [
                        StickerSendMessage(package_id=a[0],sticker_id=b[0]),
                        TextSendMessage(text='oof off'),
                        TextSendMessage(text='Plz pet my belly'),
                        TextSendMessage(text='Is it dinner time?'),
                        StickerSendMessage(package_id=a[0],sticker_id=b[0]),
                        TextSendMessage(text='Remember to drink water!'),
                        TextSendMessage(text='So tired zzz'),
                        TextSendMessage(text=event.message.text),
                        StickerSendMessage(package_id=a[0],sticker_id=b[0])
                    ]
            random.shuffle(message)
            line_bot_api.reply_message(event.reply_token,message[0])
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))

def reminders(event):
    try:
        message = TemplateSendMessage(
                alt_text= 'Reminder Selecting Menu',
                template = ButtonsTemplate(
                        #thumbnail_image_url=,
                        title='Let me remember things for you!',
                        text='What do you need?',
                        actions=[
                                PostbackTemplateAction(
                                        label='add',
                                        data='action=add',
                                ),
                                PostbackTemplateAction(
                                        label='edit',
                                        data='action=edit',
                                ),
                                PostbackTemplateAction(
                                        label='delete',
                                        data='action=delete',
                                ),
                                MessageTemplateAction(
                                        label='Look Up',
                                        text='ShowAllReminders',
                                ),        
                                ]
                            )
                        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def addreminder(event, backdata):
     try:
         
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Please Say: #[TaskName]\nFor example: #Go to Gym'))
        
     except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def editreminder(event, backdata):
     try:
        message = TextSendMessage(
                text = "Please say: edit[TaskName]\nFor eample: edit Go to Gym"
                )
        line_bot_api.reply_message(event.reply_token,message)
     except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def getreminder(event):
    cName=event.message.text[1:]

    try:
        if  reminder.objects.filter(cName='{}'.format(cName)).count()>0:
            message=TextSendMessage(text='I know this. Dont worry. I got you!')
        else:
            message = TemplateSendMessage(
                    alt_text= 'Schedule Menu',
                    template = ButtonsTemplate(
                            #thumbnail_image_url=,
                            title='Do you need me to remind you in a specific time?',
                            text='Please Select:',
                            
                            actions=[
                                    PostbackTemplateAction(
                                            label='Yeah sure',
                                            data='action=time&item={}'.format(str(cName)),
                                    ),
                                    PostbackTemplateAction(
                                            label='Nah, Its ok',
                                            data='action=notime&item={}'.format(str(cName)),
                                    ),        
                                    ]
                                )
                            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def gettime(event, backdata):
    cName=backdata.get('item')
    mintime=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
    try:
        message=TemplateSendMessage(
                alt_text='Time Menu',
                template=ButtonsTemplate(
                        title='Please Select Time',
                        text='Time Selecting:',
                        actions=[
                                DatetimePickerTemplateAction(
                                        label="Selecting Day/Time",
                                        data="action=sell&item={}".format(str(cName)),
                                        mode="datetime",
                                        #initial="time.localtime()",
                                        min=mintime,
                                        #max="2050-12-31T23:59"
                                        ),
                                ]
                            )
                        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def sendtime(event, backdata):
    try:
        to = event.source.user_id
        dt=datetime.datetime.strptime(event.postback.params.get('datetime'),'%Y-%m-%dT%H:%M')
        time = dt
        dtext=dt.strftime('{g}\n{d}%Y-%m-%d\n{t}%H:%M').format(g=backdata.get('item'),d='Day:',t='Time:')
        message = TextSendMessage(
                text = 'OK~OK~\n'+dtext
                )
    #        dt=dt.astimezone(pytz.utc)
        unit=reminder.objects.create(cName=backdata.get('item'),cTime=time,cid=to)
        unit.save()
    #    to = event.source.user_id
    #    print(to)
    
        line_bot_api.reply_message(event.reply_token,message)
        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def notime(event, backdata):
    cName=backdata.get('item')
    to = event.source.user_id
    try:
        message = TextSendMessage(
                text = "I will write down this:{}".format(str(cName))
                )
        
        unit=reminder.objects.create(cName=backdata.get('item'),cid=to)
        unit.save()
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def job():
    try:
        
#       target=reminder.objects.all().filter(cTime=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'))
        target=reminder.objects.all().exclude(cTime=None).order_by('cTime')[:1]
        s=switch.objects.get(switch='{}'.format('switch'))
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        
        # global nTimer
        # # 子執行緒的工作函數    
        # nTimer = Timer(10, job)
        if target.count() == 0:
            print("null")
        else:
            if str(target[0].cTime)[:-3] == datetime.datetime.now().strftime('%Y-%m-%d %H:%M'):
                a=['Just do it','Dont procrastinate','~~~']
                random.shuffle(a)
                message=[TextSendMessage(
                        text=a[0]+'\nDing!Ding\nIt is time to\'{}\''.format(str(target[0].cName))
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
    except:
        target=reminder.objects.all().exclude(cTime=None).order_by('cTime')[:1]
        line_bot_api.push_message(target[0].cid,TextSendMessage(text='Reminder Error'))
        # nTimer.cancel()
    
def deletereminder(event, backdata):
     try:
        message = TextSendMessage(
                text = "Please type: delete\nFor example: delete wake up"
                )
        line_bot_api.reply_message(event.reply_token,message)
     except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def edit(event):
    Name=event.message.text[2:]
    to = event.source.user_id
    mintime=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
    try:
        if reminder.objects.filter(cName=Name,cid=to).count()>0:
            
            message=TemplateSendMessage(
                    alt_text='time template',
                    template=ButtonsTemplate(
                            title='Someting wrong?Dont worry',
                            text='I got you:',
                            actions=[
                                    DatetimePickerTemplateAction(
                                            label="Select a time",
                                            data="action=selledit&item={}".format(str(Name)),
                                            mode="datetime",
                                            #initial="time.localtime()",
                                            min=mintime,
                                            #max="2050-12-31T23:59"
                                            ),
                                    ]
                                )
                            )
            
            line_bot_api.reply_message(event.reply_token,message)
        else:
            line_bot_api.reply_message(event.reply_token,message=[TextSendMessage(text='Wait I dont remember. Let me check'),StickerSendMessage(package_id=11539,sticker_id=52114129)])
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand')) 
def edittime(event, backdata):
    try:
        to = event.source.user_id
        Name=backdata.get('item')
        target=reminder.objects.get(cName='{}'.format(Name),cid=to)
        dt=datetime.datetime.strptime(event.postback.params.get('datetime'),'%Y-%m-%dT%H:%M')
        dtext=dt.strftime('{h}{g}\n{d}%Y-%m-%d\n{t}%H:%M').format(h=backdata.get('item'),g='Change to',d='Day:',t='Time:')
        message = TextSendMessage(
                text = 'Am I correct?\n'+dtext
                )
        target.cTime=dt
        target.save()

        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand')) 
def delete(event):
    try:
        to = event.source.user_id
        Name=event.message.text[2:]
        if reminder.objects.filter(cName=Name,cid=to).count()>0:
            message = TemplateSendMessage(
                    alt_text= 'Comfirm',
                    template = ButtonsTemplate(
                            #thumbnail_image_url=,
                            title='Do you want to delete{}?'.format(Name),
                            text='Are you sure?',
                            
                            actions=[
                                    PostbackTemplateAction(
                                            label='Yes, I dont want it anymore',
                                            data='action=yesdelete&item={}'.format(str(Name)),
                                    ),
                                    PostbackTemplateAction(
                                            label='Wait a second',
                                            data='action=nodelete&item={}'.format(str(Name)),
                                    ),        
                                    ]
                                )
                            )
            line_bot_api.reply_message(event.reply_token,message)
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Wait I dont remember this. Let me check'))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def yesdelete(event, backdata):
    try:
        to = event.source.user_id
        Name=backdata.get('item')
        target=reminder.objects.get(cName='{}'.format(Name),cid=to)
        target.delete()
        message = TextSendMessage(
                text = 'Wait. I erased all!\n.\n.\n.\nJust kidding\n I just delete'+str(Name)+''
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def nodelete(event, backdata):
    try:
        message = TextSendMessage(
                text = 'Okay Dont trick me again'
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
def checkreminder(event):
    try:
        to = event.source.user_id
        a=''
        c=0
        if reminder.objects.filter(cid=to).count() > 0:
            target =list(reminder.objects.filter(cid=to).order_by('-cTime').values_list('cName', 'cTime'))
            for p in target:
                
                if p[1]==None:
                    if c==0:
                        a=a+'\t\tReminders:\t\t\n'
                        c=c+1
                        
                    b=('{n}\n'.format(n=p[0]))
                else:
                    b=('{n} {t}\n'.format(n=p[0],t=str(p[1])[:-3]))
                a=a+b
                
            message = TextSendMessage(
                    text = a[:-1]
                    )
            line_bot_api.reply_message(event.reply_token,message)
        else:
            message= [TextSendMessage(text = 'All done!'),TextSendMessage(text = 'Its empty. Nice job!')]
            random.shuffle(message)
            line_bot_api.reply_message(event.reply_token,message[0])
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))

def learn(event):
    try:
        received_text = event.message.text[6:]
        semicolon_index = received_text.find(';')
        if semicolon_index == -1:
            semicolon_index = received_text.find('；')
            if semicolon_index == -1 or semicolon_index == 0 or received_text[-1]== ';' or received_text[-1] == '；':
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
        if talk.objects.filter(cget=received_text[:semicolon_index]).count()>0:
            unit=talk.objects.get(cget=received_text[:semicolon_index])
            unit.csay=received_text[semicolon_index+1:]
            unit.save()
        
        else:           
            unit=talk.objects.create(cget=received_text[:semicolon_index],csay=received_text[semicolon_index+1:])
            unit.save()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Lets chat~'))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))

def learn2(event):
    try:
        received_text = event.message.text[3:]
        semicolon_index = received_text.find(';')
        if semicolon_index == -1:
            semicolon_index = received_text.find('；')
            if semicolon_index == -1 or semicolon_index == 0 or received_text[-1]== ';' or received_text[-1] == '；':
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
        if talk.objects.filter(cget=received_text[:semicolon_index]).count()>0:
            unit=talk.objects.get(cget=received_text[:semicolon_index])
            unit.csay=received_text[semicolon_index+1:]
            unit.save()
        
        else:           
            unit=talk.objects.create(cget=received_text[:semicolon_index],csay=received_text[semicolon_index+1:])
            unit.save()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Ive learned it!'))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))

def forget(event):
    try:
        received_text = event.message.text[8:]
        if talk.objects.filter(cget=received_text).count()>0:
            target=talk.objects.filter(cget=received_text)
            target.delete()
        
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Ive forgotten'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont know this in the first place'))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand')) 

def forget2(event):
    try:
        received_text = event.message.text[5:]
        print(received_text)
        if talk.objects.filter(cget=received_text).count()>0:
            target=talk.objects.filter(cget=received_text)
            target.delete()
        
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Ive forgottn'))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont know this actually'))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand')) 

def checktalk(event):
    try:
        a=''
        target =list(talk.objects.values_list('csay', 'cget'))
        for p in target:
            b='{a};{b}\n-----------------------------\n' .format(a=p[1],b=p[0])
            a=a+b
        message = TextSendMessage(
                text ='I know these words:\n' + a[:-1]
                )
        line_bot_api.reply_message(event.reply_token,message)    
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))

def getmoney(event):
    try:
        to = event.source.user_id
        cmoney=event.message.text[1:]
        if cmoney.find('/') == -1:
            message=TextSendMessage(
                text='Select a Category:',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(
                                label='Food',
    
                                data='action=food&item1={a}&item2={b}'.format(a=cmoney,b=to)
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Transportation',
                                                 data='action=trans&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Grocery',
                                                 data='action=daily&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Entertainment',
                                                 data='action=entertainment&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Clothing',
                                                 data='action=cloth&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Medical',
                                                 data='action=medical&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label='Others',
                                                 data='action=other&item1={a}&item2={b}'.format(a=cmoney,b=to))
                            ),
                        ]
                ))
            line_bot_api.reply_message(event.reply_token,message)
        else:
            a=0        
            received_text = cmoney
            index = received_text.find('/')
            if int(received_text[:index])>0:
            
                c=received_text[index+1:]
                to = event.source.user_id
                temp=datetime.datetime.now()
                unit=money.objects.create(cmoney=int(received_text[:index]),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass=c,ccid=to)
                unit.save()
                target=list(money.objects.filter(cclass=c,ccid=to,cmonth=str(temp.month)).values_list('cmoney'))
                for p in target:
                    
                     a=a+int(p[0])
                
                message='(Sniff Sniff)What did you buy?'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message+'\nI have\"'+c+'\"added{a}dollars\nin this month\"'.format(a=received_text[index])+c+'\"已經花了{b}元囉'.format(b=a)))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Please enter a price number'))
            
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def food(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass='Food',ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass='Food',ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
            num=num+int(p[0])
        a=[TextSendMessage(text='Looks delicious'),TextSendMessage(text='Stay full'),TextSendMessage(text='I am hungry now'),TextSendMessage(text='Can I have a bite?'),TextSendMessage(text='Eat and grow!')]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I have added in\"Food\"with{a}dollars\nYou have spent{{b} dollars in \"Food\" this month}'.format(a=backdata.get('item1'),b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def trans(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass='Transportation',ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass='Transportation',ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
             num=num+int(p[0])
        
        a=[TextSendMessage(text='I am faster than you'),TextSendMessage(text='I am speed'),TextSendMessage(text='Let\'s go'),TextSendMessage(text='I want to go too'),TextSendMessage(text='Wish I can go with you next time~')]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I\'ve added in\"Transportation\"with{a}dollars\nYou have spent {b} dollars in Tranportation this month'.format(a=backdata.get('item1'),b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def daily(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        c='grocery'
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass=c,ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass=c,ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
             num=num+int(p[0])
        
        a=[TextSendMessage(text='I want that!'),TextSendMessage(text='Nice choice!'),TextSendMessage(text='Is it for me?'),TextSendMessage(text='Hmm'),TextSendMessage(text='Save some money')]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I have\"'+c+'\"add{a}dollars\n\"'.format(a=backdata.get('item1'))+c+'\"You have spent{b}dollars this month'.format(b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def entertainment(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        c='Entertainment'
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass=c,ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass=c,ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
             num=num+int(p[0])
        
        a=[TextSendMessage(text='Let\'s go outside and play~'),TextSendMessage(text='Bring with me!'),TextSendMessage(text='Oh yeah~It\'s fun'),StickerSendMessage(package_id=11539,sticker_id=52114116)]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I\'ve add\"'+c+'\"{a}dollars\n\"'.format(a=backdata.get('item1'))+c+'\"you have spent{b}dollars this month'.format(b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def cloth(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        c='衣服'
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass=c,ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass=c,ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
             num=num+int(p[0])
        
        a=[TextSendMessage(text='Looks great'),TextSendMessage(text='It\s too big for me'),TextSendMessage(text='Is that my new shirts?'),StickerSendMessage(package_id=11538,sticker_id=51626521 )]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I\'ve added\"'+c+'\"{a}dollars\n\"'.format(a=backdata.get('item1'))+c+'\"You have spent{b}dollars this month'.format(b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def medical(event, backdata):
    try:
        num=0
        temp=datetime.datetime.now()
        c='醫療'
        unit=money.objects.create(cmoney=backdata.get('item1'),cyear=str(temp.year),cmonth=str(temp.month),cday=str(temp.day),cclass=c,ccid=backdata.get('item2'))
        unit.save()
        target=list(money.objects.filter(cclass=c,ccid=backdata.get('item2'),cmonth=str(temp.month)).values_list('cmoney'))
        for p in target:
            
             num=num+int(p[0])
        
        a=[TextSendMessage(text='What happened'),TextSendMessage(text='Did you fall again?'),TextSendMessage(text='God bless you'),StickerSendMessage(package_id=11538,sticker_id=51626511)]
        random.shuffle(a)
        message=[a[0],TextSendMessage(text='I\'ve add\"'+c+'\"{a}dollars\n\"'.format(a=backdata.get('item1'))+c+'\"You have spent{b}dollars this month'.format(b=num))]
        line_bot_api.reply_message(event.reply_token,message)
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        
def other(event, backdata):
    try:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Not like this~\n Please enter: $[Price]/[Category]\nFor example: $∞/My love'))
        
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
        

def example(event):
    try:
        message = TemplateSendMessage(
            alt_text= 'Options template',
            template = ButtonsTemplate(
                    #thumbnail_image_url=,
                    title='123',
                    text='Something wrong?',
                    actions=[
                            PostbackTemplateAction(
                                    label='I want to add an expense',
                                    data='action=forget',
                            ),
                            PostbackTemplateAction(
                                    label='I want to edit',
                                    data='action=delete$',
                            ),
                            PostbackTemplateAction(
                                    label='I want to check my expenses',
                                    data='action=3',
                            ),        
                            ]
                        )
                    )
        line_bot_api.reply_message(event.reply_token,message)
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I dont understand'))
            
def forgetmoney(event,backdata):
    try:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Not like this~\n Please enter: +$[Price]/[Category]\n例如:+$12/bobba tea'))
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='我搞糊塗了汪'))
        
def deleteexample(event,backdata):
    try:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Not like this~\n Please enter: -$[Price]/[Category]\n例如:-$520/TV'))
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def editmoney(event):
    try:
        received_text = event.message.text[2:]
        index = received_text.find('/')
        if int(received_text[:index])>0:
            cclass = received_text[index+1:]
            cmoney = received_text[:index]
            message=TemplateSendMessage(
                        alt_text='Time template',
                        template=ButtonsTemplate(
                                title='Choose a date',
                                text='testing',
                                actions=[
                                        DatetimePickerTemplateAction(
                                                label="Click here",
                                                data="action=1&item1={a}&item2={b}".format(a=cmoney,b=cclass),
                                                mode="date",
                                                ),
                                        ]
                                    )
                                )
                
            line_bot_api.reply_message(event.reply_token,message)
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def moneytime(event,backdata):
    try:
        to = event.source.user_id
        cmoney=backdata.get('item1')
        cclass=backdata.get('item2')
        dt=event.postback.params.get('date')
        cyear=str(int(dt[:4]))
        cmonth=str(int(dt[5:7]))
        cday=str(int(dt[8:]))
        unit=money.objects.create(cmoney=cmoney,cyear=cyear,cmonth=cmonth,cday=cday,cclass=cclass,ccid=to)
        unit.save()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I\'ve add{y}-{m}-{d}in \'{a}\'with{b}dollars'.format(y=cyear,m=cmonth,d=cday,a=cclass,b=cmoney)))
          
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def deletemoney(event):
    try:
        received_text = event.message.text[2:]
        index = received_text.find('/')
        if int(received_text[:index])>0:
            cclass = received_text[index+1:]
            cmoney = received_text[:index]
            message=TemplateSendMessage(
                        alt_text='Time Template',
                        template=ButtonsTemplate(
                                title='testing',
                                text='Select:',
                                actions=[
                                        DatetimePickerTemplateAction(
                                                label="testing",
                                                data="action=2&item1={a}&item2={b}".format(a=cmoney,b=cclass),
                                                mode="date",
                                                ),
                                        ]
                                    )
                                )
                
            line_bot_api.reply_message(event.reply_token,message)
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def deletemoneytime(event, backdata):
    try:
        to = event.source.user_id
        cmoney=backdata.get('item1')
        cclass=backdata.get('item2')
        dt=event.postback.params.get('date')
        cyear=str(int(dt[:4]))
        cmonth=str(int(dt[5:7]))
        cday=str(int(dt[8:]))
        unit=money.objects.filter(cmoney=cmoney,cyear=cyear,cmonth=cmonth,cday=cday,cclass=cclass,ccid=to)
        unit[0].delete()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='{y}-{m}-{d}I\'ve delete\'{a}\'with{b}dollars'.format(y=cyear,m=cmonth,d=cday,a=cclass,b=cmoney)))
    except:    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def checkexample(event):
    try:
        message=TextSendMessage(
                text='You can look up total by typing: $MySpending\'[]Time\'\nFor example: $MySpending2020/5/6\n, $MySpending2020/1\n, $MySpending2020\n, or just select',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(
                                label='Today',
    
                                data='action=today'
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(
                                label='Yesterday',
    
                                data='action=yesterday'
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(
                                label='This Month',
    
                                data='action=thismonth'
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(
                                label='Last Month',
    
                                data='action=lastmonth'
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(
                                label='This Year',
    
                                data='action=thisyear'
                                )
                            ),
                        QuickReplyButton(
                            action=PostbackAction(
                                label='Last Year',
    
                                data='action=lastyear'
                                )
                            ),
                        ]
                )
                )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='123'))
        
def today(event, backdata):
    try:
        to = event.source.user_id
        temp=datetime.date.today()
        cyear=str(int(temp.year))
        cmonth=str(int(temp.month))
        cday=str(int(temp.day))
        unit=money.objects.filter(cyear=cyear,cmonth=cmonth,cday=cday,ccid=to).order_by('cclass')
        message='Let\'s see how much you spent on{a}-{b}-{c}:\n'.format(a=cyear,b=cmonth,c=cday)
        
        for i in list(unit.values_list('cclass','cmoney')): 
            
            message=message+'{a}:{b}dollars\n'.format(a=i[0],b=i[1])
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
                
def yesterday(event, backdata):
    try:
        to = event.source.user_id
        temp=datetime.date.today() - datetime.timedelta(days=1)
        cyear=str(int(temp.year))
        cmonth=str(int(temp.month))
        cday=str(int(temp.day))
    
        unit=money.objects.filter(cyear=cyear,cmonth=cmonth,cday=cday,ccid=to).order_by('cclass')
        message='Let\'s see howmuch you spent on{a}-{b}-{c}:\n'.format(a=cyear,b=cmonth,c=cday)
        
        for i in list(unit.values_list('cclass','cmoney')): 
            
            message=message+'{a}:{b}dollars\n'.format(a=i[0],b=i[1])
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def thismonth(event, backdata):
    try:
        to = event.source.user_id
        temp=datetime.date.today()
        cyear=str(int(temp.year))
        cmonth=str(int(temp.month))
        
    
        unit=money.objects.filter(cyear=cyear,cmonth=cmonth,ccid=to).order_by('cclass')
        message='Let\'s see how much you spent on{a}-{b}:\n'.format(a=cyear,b=cmonth)
        i=None
        for cclass in list(unit.values_list('cclass')):
            if i==cclass[0]:
                print(i)
                i=cclass[0]
                pass
            else:
                i=cclass[0]  
                a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                num=0
                for p in a:
                    num=num+int(p[0])
                message=message+'{a}:{b}dollars\n'.format(a=cclass[0],b=num)
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def lastmonth(event, backdata):
   try:
        to = event.source.user_id
        temp=datetime.date.today() - datetime.timedelta(months=1)
        cyear=str(int(temp.year))
        cmonth=str(int(temp.month))
    
        unit=money.objects.filter(cyear=cyear,cmonth=cmonth,ccid=to).order_by('cclass')
        message='Let\'s see how much you spent on{a}-{b}:\n'.format(a=cyear,b=cmonth)
        i=None
        for cclass in list(unit.values_list('cclass')):
            if i==cclass[0]:
                print(i)
                i=cclass[0]
                pass
            else:
                i=cclass[0]  
                a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                num=0
                for p in a:
                    num=num+int(p[0])
                message=message+'{a}:{b}dollars\n'.format(a=cclass[0],b=num)
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
   except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def thisyear(event, backdata):
    try:
        to = event.source.user_id
        temp=datetime.date.today()
        cyear=str(int(temp.year))
    
        unit=money.objects.filter(cyear=cyear,ccid=to).order_by('cclass')
        message='Let\'s see how much you spent on{a}:\n'.format(a=cyear)
        i=None
        for cclass in list(unit.values_list('cclass')):
            if i==cclass[0]:
                print(i)
                i=cclass[0]
                pass
            else:
                i=cclass[0]  
                a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                num=0
                for p in a:
                    num=num+int(p[0])
                message=message+'{a}:{b}dollars\n'.format(a=cclass[0],b=num)
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def lastyear(event, backdata):
    try:
        to = event.source.user_id
        temp=datetime.date.today() - datetime.timedelta(years=1)
        cyear=str(int(temp.year))
    
        unit=money.objects.filter(cyear=cyear,ccid=to).order_by('cclass')
        message='Leet\'s see how much you spent on{a}:\n'.format(a=cyear)
        i=None
        for cclass in list(unit.values_list('cclass')):
            if i==cclass[0]:
                print(i)
                i=cclass[0]
                pass
            else:
                i=cclass[0]  
                a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                num=0
                for p in a:
                    num=num+int(p[0])
                message=message+'{a}:{b}dollars\n'.format(a=cclass[0],b=num)
            
    
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
        
def checkmoney(event):
    try:
        text=event.message.text[3:]
        to = event.source.user_id
        cyear=text[:4]
        if len(text)>4:
            temp=text[5:]
            index=temp.find('/')
            if  index != -1:
                cday=str(int(temp[index+1:]))
                cmonth=str(int(temp[:index]))
                unit=money.objects.filter(cyear=cyear,cmonth=cmonth,cday=cday,ccid=to).order_by('cclass')
                message='Let\'s see how much you spent on{a}-{b}-{c}:\n'.format(a=cyear,b=cmonth,c=cday)
                for i in list(unit.values_list('cclass','cmoney')): 
            
                    message=message+'{a}:{b}dollars\n'.format(a=i[0],b=i[1])
                    
            
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
            else:
                cmonth=str(int(text[5:]))  
                unit=money.objects.filter(cyear=cyear,cmonth=cmonth,ccid=to).order_by('cclass')
                message='Let\'s see how much you spent on{a}-{b}:\n'.format(a=cyear,b=cmonth)
            
                i=None
                for cclass in list(unit.values_list('cclass')):
                    if i==cclass[0]:
                        print(i)
                        i=cclass[0]
                        pass
                    else:
                        i=cclass[0]  
                        a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                        num=0
                        for p in a:
                            num=num+int(p[0])
                        message=message+'{a}:{b}dollars\n'.format(a=cclass[0],b=num)
                
        
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
        else:
            unit=money.objects.filter(cyear=cyear,ccid=to).order_by('cclass')
            message='Let\'s see how much you spent on{a}:\n'.format(a=cyear)
            i=None
            for cclass in list(unit.values_list('cclass')):
                if i==cclass[0]:
                        print(i)
                        i=cclass[0]
                        pass
                else:
                    a=list(unit.filter(cclass=cclass[0]).values_list('cmoney'))
                    num=0
                    for p in a:
                        num=num+int(p[0])
                    message=message+'{a}:{b}元\n'.format(a=cclass[0],b=num)
                
        
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message[:-1]))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I don\'t understand'))
def switchon(event):
    try:
        if switch.objects.filter(switch='switch').count() > 0 :
        
            s=switch.objects.get(switch='{}'.format('switch'))
            if s.num == 0:
                
                s.num=1
                s.save()
                job()
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Open Reminder'))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='You\'ve already opened it'))
        else:
            unit=switch.objects.create(switch='switch',num=1)
            unit.save()
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Error'))

def switchoff(event):
    try:       
        s=switch.objects.get(switch='{}'.format('switch'))
        s.num=0
        s.save()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Close Reminder'))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Error'))
        

def imagereply(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='WoW, WhAt Is ThIs??'))  
    
    
        
    
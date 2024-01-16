from django.contrib import admin
from test2api.models import reminder, talk, money, switch
# Register your models here.

class reminderAdmin(admin.ModelAdmin):
    list_display=('id','cName','cTime','cid')
    list_filter=('cName','cTime','cid')
    search_fields=('cName',)
    ordering=('cTime',)
    
admin.site.register(reminder,reminderAdmin)

class talkAdmin(admin.ModelAdmin):
    list_display=('id','cget','csay')
    list_filter=('cget','csay')
    search_fields=('cget','csay',)
    ordering=('cget',)
    
admin.site.register(talk,talkAdmin)

class moneyAdmin(admin.ModelAdmin):
    list_display=('id','cmoney','cyear','cmonth','cday','cclass','ccid')
    list_filter=('cmoney','cclass','ccid','cyear','cmonth','cday')
    search_fields=('cmoney','cclass','cyear','cmonth','cday',)
    ordering=('cmonth',)
    
admin.site.register(money,moneyAdmin)

class switchAdmin(admin.ModelAdmin):
    list_display=('id','num', 'switch')
    list_filter=('id','num','switch')
    search_fields=('num',)
    ordering=('num',)
    
admin.site.register(switch,switchAdmin)
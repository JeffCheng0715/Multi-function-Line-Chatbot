from django.db import models

class reminder(models.Model):
    cName=models.CharField(max_length=20, null= False)
    cTime=models.CharField(max_length=20, null= True,blank=True)
    cid=models.CharField(max_length=100, null= False, default="")
    
    def __str__(self):
        return self.cName
    
class talk(models.Model):
    cget=models.CharField(max_length=20, null= False)
    csay=models.CharField(max_length=20, null= False)
    
    def __str__(self):
        return self.cget
    
class money(models.Model):
    cmoney=models.IntegerField(null= False)
    cyear=models.CharField(max_length=4, null= False, default="")
    cmonth=models.CharField(max_length=2, null= False, default="")
    cday=models.CharField(max_length=2, null= False, default="")
    cclass=models.CharField(max_length=20, null= False)
    ccid=models.CharField(max_length=100, null= False, default="")
    
    def __str__(self):
        return self.ccid
    
class switch(models.Model):
    num=models.IntegerField(null= True)
    switch=models.CharField(max_length=20, null= False , default="")
    
    
    def __str__(self):
        return self.switch

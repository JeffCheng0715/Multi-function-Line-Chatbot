# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:32:54 2020

@author: jeffc
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import os
# Declare a scheduler
sched = BlockingScheduler()

# execute def scheduled_jog() every 1 minute
@sched.scheduled_job('interval', minutes=1)
def scheduled_job():
    print("do timer")
    os.system("python timer.py")

sched.start()
#!/usr/bin/env python

import schedule
import subprocess
import time


def job():
    subprocess.call(['aplay /home/pi/Music/teste.wav'], shell=True)


schedule.every().day.at('16:15').do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

import schedule
import time
import os

def job():
    os.system("shutdown -r -t 0 -f")

schedule.every().day.at("04:41").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
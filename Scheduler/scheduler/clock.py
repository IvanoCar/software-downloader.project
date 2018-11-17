from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from scheduler.modules.scraper import Scraper
import json
from threading import Thread

sched = BlockingScheduler()


@sched.scheduled_job('interval', hours=24)
def sync_download_links():
    API_URL = 'DOMAIN/update/all'
    API_KEY = 'KEY GOES HERE'
    headers = {
        'user-agent': 'software-downloader.cron',
        'api-key': API_KEY
    }
    s = Scraper()
    if s.error:
        pass
    # Thread(target=s.notify).start()
    r = requests.post(API_URL,
                      json=json.loads(json.dumps({'results': s.ddlinks})), headers=headers)
    print('Sync done.', r.text, 'error:', s.error)


sched.start()

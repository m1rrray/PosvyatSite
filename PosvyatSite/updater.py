from apscheduler.schedulers.background import BackgroundScheduler

from google_sheets import save_datatransfer_to_google, save_dataregistration_to_google, save_dataresettlement_to_google


def start_transfer():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_datatransfer_to_google, 'interval', minutes=3)
    scheduler.start()


def start_resettlement():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_dataresettlement_to_google, 'interval', minutes=3)
    scheduler.start()


def start_registration():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_dataregistration_to_google, 'interval', minutes=3)
    scheduler.start()

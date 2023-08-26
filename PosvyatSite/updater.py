from apscheduler.schedulers.background import BackgroundScheduler

from google_sheets import save_transfer_to_google, save_registration_to_google, save_resettlement_to_google


def start_transfer():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_transfer_to_google, 'interval', minutes=3)
    scheduler.start()


def start_resettlement():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_resettlement_to_google, 'interval', minutes=3)
    scheduler.start()


def start_registration():
    scheduler = BackgroundScheduler()
    scheduler.add_job(save_registration_to_google, 'interval', minutes=3)
    scheduler.start()

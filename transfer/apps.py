from django.apps import AppConfig


class TransferConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transfer'

    def ready(self):
        from PosvyatSite import updater
        updater.start_transfer()

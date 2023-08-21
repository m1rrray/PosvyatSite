from django.apps import AppConfig


class ResettlementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resettlement'

    def ready(self):
        from PosvyatSite import updater
        updater.start_resettlement()
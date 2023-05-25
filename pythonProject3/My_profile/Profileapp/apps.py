from django.apps import AppConfig


class ProfileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Profileapp'

    def ready(self):
        import Profileapp.signals

from django.apps import AppConfig


class VerifcationOtpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'verifcation_otp'

    def ready(self):
        import verifcation_otp.signals
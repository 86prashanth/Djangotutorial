from django.apps import AppConfig


class ModelRelationshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_relationship'

    def ready(self):
        import model_relationship.signals
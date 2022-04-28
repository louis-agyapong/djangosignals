from django.apps import AppConfig


class BuyersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangosignals.buyers"

    def ready(self) -> None:
        from djangosignals.buyers import signals # noqa: F401

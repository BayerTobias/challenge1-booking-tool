from django.apps import AppConfig


class BookingToolConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "booking_tool"

    def ready(self):
        import booking_tool.signals

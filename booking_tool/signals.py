from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Doctor, Patient


@receiver(post_delete, sender=Doctor)
def delete_user_with_doctor(sender, instance, **kwargs):
    """
    Signal receiver function to delete associated User object when a Doctor instance is deleted.
    """
    if instance.user:
        instance.user.delete()


@receiver(post_delete, sender=Patient)
def delete_user_with_patient(sender, instance, **kwargs):
    """
    Signal receiver function to delete associated User object when a Patient instance is deleted.
    """
    if instance.user:
        instance.user.delete()

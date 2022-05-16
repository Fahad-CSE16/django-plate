from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class StatusChoices(models.TextChoices):
    ACTIVE = 'active', 'active'
    INACTIVE = 'inactive', 'inactive'
    

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='updated_%(class)ss', null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'base'

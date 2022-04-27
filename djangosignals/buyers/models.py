from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signal = models.BooleanField(_("From Signal"), default=False)

    def __str__(self):
        return self.user.username

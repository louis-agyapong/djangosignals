from tkinter.tix import NoteBook
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangosignals.buyers.models import Buyer

import uuid


class Car(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(_("Code"), max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4()).replace("-", "")[:10]
        super().save(*args, **kwargs)

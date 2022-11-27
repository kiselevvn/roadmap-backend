from django.db import models
from django.utils.translation import gettext_lazy as _


class Roadmap(models.Model):
    """
    Модель дорожной карты
    """

    name = models.CharField(_("Наименование"), max_length=150)
    description = models.TextField(_("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = _("Дорожная карта")
        verbose_name_plural = _("Дорожные карты")


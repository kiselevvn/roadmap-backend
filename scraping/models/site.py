from django.db import models
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    """
    Информация о сайтах
    """

    name = models.CharField(_("Наименование"), max_length=150)
    domain = models.URLField(_("Домен"), max_length=200)

    class Meta:
        verbose_name = _("Сайт")
        verbose_name_plural = _("Сайты")


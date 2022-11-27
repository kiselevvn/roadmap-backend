from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteParam(models.Model):
    """
    Параметры сайта
    для парсинга
    """

    block = models.ForeignKey(
        to="roadmaps.Block",
        on_delete=models.CASCADE,
        verbose_name=_("Родитель"),
        blank=True, null=True
    )
    site = models.ForeignKey(
        to="scraping.Site",
        on_delete=models.CASCADE,
        verbose_name=_("Сайт"),
        blank=True, null=True
    )
    param = models.TextField(_("Параметры парсера"), blank=True, null=True)

    class Meta:
        unique_together = ("block","site")
        verbose_name = _("Параметры сайта")
        verbose_name_plural = _("Параметры сайтов")


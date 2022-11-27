from django.db import models
from django.utils.translation import gettext_lazy as _


class Response(models.Model):
    """
    Резултаты парсинга
    """

    last_update = models.DateTimeField(_("Последнее обновление"), auto_now=False, auto_now_add=False, blank=True, null=True)
    result = models.TextField(_("Результат"), blank=True, null=True)
    site_param = models.ForeignKey(
        to="roadmaps.SiteParam",
        on_delete=models.CASCADE,
        verbose_name=_("Параметры сайта"),
    )


    class Meta:
        verbose_name = _("Резултат парсинга")
        verbose_name_plural = _("Резултаты парсинга")


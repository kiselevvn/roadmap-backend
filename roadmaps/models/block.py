from django.db import models
from django.utils.translation import gettext_lazy as _


class Block(models.Model):
    """
    Модель блока дорожной карты
    """

    roadmap = models.ForeignKey(
        to="roadmaps.Roadmap",
        on_delete=models.CASCADE,
        verbose_name=_("Дорожная карта"),
        blank=True, null=True
    )
    name = models.CharField(_("Наименование"), max_length=150)
    description = models.TextField(_("Описание"), blank=True, null=True)
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        verbose_name=_("Родитель"),
        blank=True, null=True
    )


    class Meta:
        verbose_name = _("Блок")
        verbose_name_plural = _("Блок")


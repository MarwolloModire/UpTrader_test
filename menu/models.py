from django.db import models
from django.utils.text import slugify


class BaseMenu(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text='This field is required. Enter the name.'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Menu(BaseMenu):
    pass


class MenuItem(BaseMenu):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        help_text='This field is required. Select the menu to which this item belongs.'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        help_text='This field is required. Select the parent item if it exists.'
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='This field is optional. Enter a URL or leave it empty to auto-generate.'
    )

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None) -> None:
        if not self.named_url:
            self.named_url = f'{slugify(self.menu)}_{slugify(self.name)}'
        super().save()

    @property
    def children(self) -> models.QuerySet:
        return self.children.all()

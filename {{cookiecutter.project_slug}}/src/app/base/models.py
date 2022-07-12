from typing import Any, Dict

from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def get_contenttype(cls) -> ContentType:
        return ContentType.objects.get_for_model(cls)

    def update_from_kwargs(self, **kwargs: Dict[str, Any]) -> None:
        """
        A shortcut method to update model instance from the kwargs.
        """
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def setattr_and_save(self, key: str, value: Any) -> None:
        """
        Shortcut for testing -- set attribute of the model and save
        """
        setattr(self, key, value)
        self.save()

    @classmethod
    def get_label(cls) -> str:
        """
        Get a unique within the app model label
        """
        return cls._meta.label_lower.split('.')[-1]


class TimestampedModel(BaseModel):
    """
    Default app model that has `created_at` and `updated_at` attributes.
    """
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True,
    )

    class Meta:
        abstract = True

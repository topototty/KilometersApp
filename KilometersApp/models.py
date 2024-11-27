from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    encrypted_phone = models.TextField(verbose_name=_('Зашифрованный номер телефона'), null=True, blank=True)

    fernet = Fernet(settings.ENCRYPTION_KEY)

    @property
    def phone(self):
        # Расшифровка номера телефона при чтении
        if self.encrypted_phone:
            return self.fernet.decrypt(self.encrypted_phone.encode()).decode()
        return None

    @phone.setter
    def phone(self, value):
        # Шифрование номера телефона при записи
        if value:
            self.encrypted_phone = self.fernet.encrypt(value.encode()).decode()

    class Meta:
        verbose_name = _("Профиль")
        verbose_name_plural = _("Профили")

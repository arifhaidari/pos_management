from datetime import timedelta
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

from django.core.mail import send_mail
from django.template.loader import get_template
# from django.utils import timezone

from pos_management.utils import random_string_generator, unique_access_code_generator
#send_mail(subject, message, from_email, recipient_list, html_message)

# DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(self, phone, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not phone:
            raise ValueError("Users must have an phone number")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            phone = phone,
            full_name=full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, full_name=None, password=None):
        user = self.create_user(
                phone=phone,
                full_name=full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self, phone, full_name=None, password=None):
        user = self.create_user(
                phone=phone,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    phone               = models.CharField(max_length=255, unique=True) # validate with javascript to be filled, integer and 10 digits
    full_name           = models.CharField(max_length=255, blank=True, null=True)
    business            = models.CharField(max_length=255, blank=True, null=True)
    address             = models.CharField(max_length=255, blank=True, null=True)
    access_code         = models.CharField(max_length=255, blank=True, null=True) # generate by system
    email               = models.CharField(max_length=255, blank=True, null=True) # generate by system
    is_active           = models.BooleanField(default=True) # if true: can login without authentication of phone or email
    staff               = models.BooleanField(default=False) # staff user non superuser
    admin               = models.BooleanField(default=False) # superuser
    deal_amount         = models.CharField(max_length=255, blank=True, default=0.0)
    plain_password      = models.CharField(max_length=255, null=True, blank=True)
    start_contract_at   = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_contract_at     = models.DateField(auto_now=False, auto_now_add=False, null=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] # it is for python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.phone

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    def get_absolute_url(self):
        return reverse("dashboard:detail", kwargs={"id": self.id})
    
def pre_save_create_access_code(sender, instance, *args, **kwargs):
    if not instance.access_code:
        instance.access_code = unique_access_code_generator(instance)

pre_save.connect(pre_save_create_access_code, sender=User)

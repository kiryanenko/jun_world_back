from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    username = models.CharField(verbose_name='username', max_length=255, unique=True,
                                error_messages={'unique': 'This username is already in use'})
    email = models.EmailField(verbose_name='email', blank=True,
                              error_messages={'unique': 'This email is already in use'})
    is_active = models.BooleanField(verbose_name='active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    date_last_seen = models.DateTimeField(verbose_name='date last seen', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='birthday', blank=True, null=True)

    rating = models.IntegerField(verbose_name='rating', default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __unicode__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user = self.model( email = email , name = name )

        user.set_password(password)  # for encrypting passwords
        user.save(using=self._db)

        return user

    def create_superuser(self,email, name, password):
        """Create and save a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the sytem"""
    email = models.EmailField(max_length=255,unique = True) #create email field / unique = unique email
    name = models.CharField (max_length=255)                #for storing an email adress
    is_active = models.BooleanField(default=True)           #to determine if an email is activate
    is_staff = models.BooleanField(default=False)           # to determine if user is a super user (admin)

    objects = UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrevie full name of user"""
        return self.name

    def get_short_name(self):
        """Retrevie short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email

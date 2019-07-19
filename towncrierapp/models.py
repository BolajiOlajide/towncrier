from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from mdeditor.fields import MDTextField

from towncrierapp.enums import ADD_MESSAGE, PUBLISH_MESSAGE


class SlackUserManager(models.Manager):
    """
    A class that manages `SlackUser` model
    """

    def __init__(self, *args):
        """
        A initialization method that setup methods and properties of this class
        from its parent
        """
        super(SlackUserManager, self).__init__()

    def create_user(self, *args, **kwargs):
        """
        An instance method that creates a new user
        """
        return SlackUser(**kwargs)


class SlackUser(AbstractBaseUser):
    """
    A class that represents a `SlackUser` account
    """
    slack_id = models.CharField(unique=True, max_length=60, null=False, primary_key=True)
    handle = models.CharField(max_length=100, blank=True, null=False)
    isActive = models.BooleanField(default=True, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @classmethod
    def create(cls, user_data_dict):
        """
        A class method that creates a new user
        """
        return cls.objects.create(**user_data_dict)

    @classmethod
    def upsert(cls, **kwargs):
        if not kwargs:
            raise ValueError('You must pass in valid kwargs')
        
        slack_id = kwargs.get('slack_id')
        isActive = kwargs.get('isActive')
        handle = kwargs.get('handle')
        user = cls.objects.filter(slack_id=slack_id).first()
        if user:
            user.isActive = isActive
            user.handle = handle
            return user.save()
        return cls.create(kwargs)

    def __repr__(self):
        return f'SlackUser - {self.handle}'

    def __str__(self):
        return f'SlackUser - {self.handle}'

    def __unicode__(self):
        return f'SlackUser - {self.handle}'


class Message(models.Model):
    """
    A model that represents a message
    """
    id = models.AutoField(unique=True, primary_key=True)
    message = MDTextField()
    published = models.BooleanField(null=False, default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self):
        return f'Message - {self.id}'

    def __str__(self):
        return f'Message - {self.id}'

    def __unicode__(self):
        return f'Message - {self.id}'


class ActivityLog(models.Model):
    """
    A model that represents a message
    """
    OPERATIONS = (
        (ADD_MESSAGE, ADD_MESSAGE),
        (PUBLISH_MESSAGE, PUBLISH_MESSAGE),
    )

    id = models.AutoField(unique=True, primary_key=True)
    operation = models.CharField(max_length=20, choices=OPERATIONS, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __repr__(self):
        return f'ActivityLog - {self.id}'

    def __str__(self):
        return f'ActivityLog - {self.id}'

    def __unicode__(self):
        return f'ActivityLog - {self.id}'

from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class CustomProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(verbose_name="Date of birth")
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    photo = models.ImageField(upload_to="photo", blank=True)

    def __unicode__(self):
        return self.first_name


class Update(models.Model):

    TYPE_CHOICES = (
            ('C', 'create'),
            ('U', 'update'),
            ('D', 'delete'),
            )
    update_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    model_name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)


@receiver(post_save)
def update_callback(sender, **kwargs):
    model_name = sender._meta.object_name
    if model_name == 'Update':
        return
    update_type = 'C' if kwargs.get('created', False) else 'U'
    u = Update(update_type=update_type, model_name=model_name)
    u.save()


@receiver(post_delete)
def delete_callback(sender, **kwargs):
    model_name = sender._meta.object_name
    if model_name == 'Update':
        return
    update_type = 'D'
    u = Update(update_type=update_type, model_name=model_name)
    u.save()

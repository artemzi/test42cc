from django.db import models


class CustomProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(verbose_name="Date of birth")
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    photo = models.ImageField(upload_to="static", blank=True)

    def __unicode__(self):
        return self.first_name
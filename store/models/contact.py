from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=500, default='')

    def sendMessage(self):
        self.save()

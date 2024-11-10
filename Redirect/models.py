from django.db import models

class Referral(models.Model):
    code = models.CharField(max_length = 100, unique = True)
    redirect_url = models.URLField()

    def __str__(self):
        return self.code


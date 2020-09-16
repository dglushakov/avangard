from django.db import models


# Create your models here.

class IconAR2NS(models.Model):
    icon_ip = models.CharField(max_length=40)
    icon_creation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Icon ' + str(self.icon_ip)

    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icons"

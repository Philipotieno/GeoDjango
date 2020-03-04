from django.db import models

# Create your models here.
class Incidence(models.Model):
    name = models.CharField(max_length=20, verbose_name="Child's First Name and Last Name")
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        # verbose_name = 'Incidence'
        verbose_name_plural = "Incidences"
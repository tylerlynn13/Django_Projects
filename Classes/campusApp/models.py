from django.db import models

# Create your models here.



class UniveristyCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default=0, blank=True, null=False)

    class Meta:
        verbose_name_plural = "University Campus"

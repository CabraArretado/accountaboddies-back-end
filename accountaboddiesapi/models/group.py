from django.db import models
from django.contrib.auth.models import User
from .account import Account

class Group(models.Model):

    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    # One member is the default, if he created the group he is on the group
    size = models.PositiveSmallIntegerField(default=1) # Limit of people in the group
    population = models.PositiveSmallIntegerField() # Number of people currently in the group

    class Meta:
        verbose_name = ("Group")
        verbose_name_plural = ("Groups")


    def get_absolute_url(self):
        return reverse("Group_detail", kwargs={"pk": self.pk})
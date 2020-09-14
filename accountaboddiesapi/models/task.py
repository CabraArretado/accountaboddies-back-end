from django.db import models
from .account import Account
from .account import Account

class Task(models.Model):

    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    # One member is the default, if he created the group he is on the group
    size = models.PositiveSmallIntegerField(default=1) # Limit of people in the group
    population = models.PositiveSmallIntegerField() # Number of people currently in the group

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")


    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
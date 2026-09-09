from django.db import models


class HouseholdMember(models.Model):
    name = models.CharField(max_length=100)


class Chore(models.Model):
    title = models.CharField(max_length=200)
    assignee = models.ForeignKey(
        HouseholdMember,
        on_delete=models.PROTECT,
        related_name="chores",
    )
    due_date = models.DateField()
    is_complete = models.BooleanField(default=False)

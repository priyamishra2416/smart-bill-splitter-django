from django.db import models


class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.FloatField()

    paid_by = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE
    )

    participants = models.ManyToManyField(
        Friend,
        related_name='expenses'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def split_amount(self):

        total_people = self.participants.count()

        if total_people == 0:
            return 0

        return round(self.amount / total_people, 2)

    def __str__(self):
        return self.title
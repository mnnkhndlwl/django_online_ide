from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=20)


class Submissions(models.Model):
    ACCEPTANCE_STATUS = [
        ("S", "Success"),
        ("E", "Error"),
        ("P", "Pending")
    ]

    code = models.CharField(max_length=200000)
    language = models.CharField(max_length=100)
    submission_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=ACCEPTANCE_STATUS)
    user_input = models.CharField(max_length=200, null=True, blank=True)
    output = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

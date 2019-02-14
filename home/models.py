from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class Member(AbstractUser):
    gen = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - Gen: {}".format(self.last_name + " " + self.first_name, self.gen)

    def get_show_name(self):
        if self.last_name is not None or self.first_name is not None:
            full_name = self.last_name + " " + self.first_name
        else:
            full_name = str(self.username)
        return full_name


class Challenge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Submission(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=False)
    result = models.FloatField(null=True)

    def __str__(self):
        return "Username: {} - Challenge: {} - Time: {}".format(self.member.username, self.challenge.name, self.time)


@receiver(post_delete, sender=Submission)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)

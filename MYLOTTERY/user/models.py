from django.db import models
from knox.models import AuthToken
from django.utils import timezone

# Create your models here.
class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        # Set the deleted_at field to the current time
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class User(SoftDeleteModel):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class RefreshToken(models.Model):
    token = models.OneToOneField(AuthToken, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
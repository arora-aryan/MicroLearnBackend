from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need for your user
    # For example, a mobile number field
    # Any other custom fields or methods can be added here

    def __str__(self):
        return self.username

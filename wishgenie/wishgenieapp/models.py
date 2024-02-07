from django.db import models

# Create your models here.
class Wishes(models.Model):
    wish_title = models.CharField(max_length=100)
    wish_slug = models.CharField(max_length= 100)
    description = models.TextField(max_length = 500)
    # a wish_category foreign key is missing
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wish_title




 
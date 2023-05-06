from django.db import models


class GuestBook(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
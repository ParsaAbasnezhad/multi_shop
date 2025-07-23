from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs',blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.title

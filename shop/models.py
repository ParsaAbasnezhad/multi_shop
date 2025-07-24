from django.db import models

from home.models import Category


class Size(models.Model):
    title = models.CharField(null=True, blank=True, max_length=10, verbose_name='سایز')

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(null=True, blank=True, max_length=15, verbose_name='رنگ')

    def __str__(self):
        return self.title


class Detail(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, verbose_name='نام کالا')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='detail_img/', verbose_name='عکس')
    price = models.FloatField(verbose_name='قیمت')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    size = models.ManyToManyField(Size, blank=True, related_name='size', verbose_name='سایز')
    color = models.ManyToManyField(Color, blank=True, related_name='color', verbose_name='رنگ')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True, verbose_name='زمان')

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Detail, null=True, on_delete=models.CASCADE, related_name='information')
    text = models.TextField()

    def __str__(self):
        return self.text[:20]

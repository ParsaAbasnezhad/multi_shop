from django.db import models


class Information(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


class Size(models.Model):
    title = models.CharField(max_length=10, verbose_name='سایز')

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=15, verbose_name='رنگ')

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام کالا')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='detail_img/', verbose_name='عکس')
    price = models.FloatField(verbose_name='قیمت')
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    size = models.ManyToManyField(Size, blank=True, null=True, related_name='size', verbose_name='سایز')
    color = models.ManyToManyField(Color, blank=True, null=True, related_name='color', verbose_name='رنگ')

    def __str__(self):
        return self.title

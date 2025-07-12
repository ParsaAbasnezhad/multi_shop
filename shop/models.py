from django.db import models


class ShopList(models.Model):
    name = models.CharField(max_length=100 ,verbose_name='مدل کالا')
    description = models.TextField(verbose_name='اطلاعات کالا')
    image = models.ImageField(upload_to='shop/', verbose_name='عکس کالا')
    price = models.FloatField(verbose_name='قیمت کالا')
    status = models.BooleanField(default=False, verbose_name='موجود هست یا نه')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا ها'

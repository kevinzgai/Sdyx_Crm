# encoding=utf-8
from django.db import models


# Create your models here.
class yueke(models.Model):  # 创建粤科数据类，继承models.Model
    cinemaName = models.CharField(max_length=50, verbose_name='影院名称')
    saleName = models.CharField(max_length=20, verbose_name='销售渠道')
    tranType = models.CharField(max_length=10, verbose_name='交易类型')
    orderNum = models.CharField(max_length=20, verbose_name='订单号')
    tranTime = models.DateTimeField(verbose_name='交易时间')
    movieName = models.CharField(max_length=100, verbose_name='影片名称')
    showTime = models.DateTimeField(verbose_name='放映时间')
    seatNum = models.CharField(max_length=200, verbose_name='座位号')
    voteNum = models.IntegerField(verbose_name='票数')
    totalAmount = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='总出票金额')
    priceAmount = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='总定价金额')
    lowFare = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='最低票价')
    handFee = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='手续费')
    alwayHandFee = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='总设定手续费')
    subsidies = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='补贴')
    subsidiesParty = models.CharField(max_length=50, verbose_name='补贴方')

    def __unicode__(self):
        return self.orderNum

    class Meta:
        verbose_name = "粤科数据"
        verbose_name_plural = "粤科数据列表"
# from django.db import models
# # Create your models here.
#
# class Payload(models.Model):
#     devId = models.CharField(unique=True)
#     devTime = models.DatetimeField(unique=True)
#     time = models.DatetimeField(null=True)
#     totalActKwh = models.BigIntegerField(null=True)
#     actKwh = models.BigIntegerField(null=True)
#     totalReactKwh = models.BigIntegerField(null=True)
#     reactKwh = models.BigIntegerField(null=True)
#     gridVR = models.BigIntegerField(null=True)
#     gridVS = models.BigIntegerField(null=True)
#     gridVT = models.BigIntegerField(null=True)
#     gridAR = models.BigIntegerField(null=True)
#     gridAS = models.BigIntegerField(null=True)
#     gridAT = models.BigIntegerField(null=True)
#     gridDR = models.BigIntegerField(null=True)
#     gridDS = models.BigIntegerField(null=True)
#     gridDT = models.BigIntegerField(null=True)
#     gridPFR = models.BigIntegerField(null=True)
#     gridPFS = models.BigIntegerField(null=True)
#     gridPFT = models.BigIntegerField(null=True)
#     totalActKw = models.BigIntegerField(null=True)
#     totalReactKw = models.BigIntegerField(null=True)
#     actKwR = models.BigIntegerField(null=True)
#     actKwS = models.BigIntegerField(null=True)
#     actKwT = models.BigIntegerField(null=True)
#     reactKwR = models.BigIntegerField(null=True)
#     reactKwS = models.BigIntegerField(null=True)
#     reactKwT = models.BigIntegerField(null=True)
#     pointName = models.BigIntegerField(null=True)
#
# class kwh(models.Model):
#     transactionId =  models.PositiveSmallIntegerField(unique=True, max_length=18)
#     siteId = models.PositiveSmallIntegerField(unique=True, max_length=10)
#     engType = models.IntegerField(unique=True)
#     version = models.CharField(unique=True, max_length=18)
#     payload = models.ForeignKey(Payload, on_delete=models.CASCADE, related_name = "Payload")

#
# fems_data sql 해석해서 넣은 부분
from django.db import models


class FemsPayload(models.Model):
    payload_id = models.AutoField(primary_key=True)
    site = models.ForeignKey('FemsTrans', related_name='siteid', on_delete= models.DO_NOTHING)
    dev = models.ForeignKey('FemsTrans',related_name='devid',on_delete= models.DO_NOTHING)
    dev_time = models.ForeignKey('FemsTrans',related_name='devtime' ,on_delete= models.DO_NOTHING, db_column='dev_time')
    payload_data = models.TextField()

    class Meta:
        db_table = 'fems_payload'


class FemsTrans(models.Model):
    site_id = models.CharField(primary_key=True, max_length=15)
    dev_id = models.CharField(max_length=128)
    transaction_id = models.CharField(max_length=20)
    dev_time = models.CharField(max_length=128)
    eng_type = models.IntegerField()
    version = models.CharField(max_length=128)

    class Meta:
        db_table = 'fems_trans'
        unique_together = (('site_id', 'dev_id', 'dev_time'),)

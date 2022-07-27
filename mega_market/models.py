import uuid
from django.db import models

# Create your models here.
class ShopUnitType(models.TextChoices):
    OFFER = "OFFER"
    CATEGORY = "CATEGORY"

class ShopUnit(models.Model):
    id = models.UUIDField(
            primary_key=True,
    #        default=uuid.uuid4,
            editable=False
            )
    name = models.CharField(max_length=50)
    date = models.DateField()
    parentID = models.UUIDField(
            default=uuid.uuid4,
            editable=False,
            null=True
            )
    type = models.CharField(
            choices=ShopUnitType.choices,
            max_length=10)
    price = models.PositiveIntegerField(null=True)
#    childern = models.DictField()


class ShopUnitImport(models.Model):
    id = models.UUIDField(
            primary_key=True,
    #        default=uuid.uuid4,
            editable=False
            )
    name = models.CharField(max_length=50)
    parentID = models.UUIDField(
    #        default=uuid.uuid4,
            editable=False,
            null=True
            )
    type = models.CharField(
            choices=ShopUnitType.choices,
            max_length=10)
    price = models.PositiveIntegerField(null=True)


class ShopUnitImportRequest(models.Model):
    items = models.ForeignKey(ShopUnitImport, on_delete=models.CASCADE)
    updateDate = models.DateField()


class ShopUnitStatisticUnit(models.Model):
    id = models.UUIDField(
            primary_key=True,
    #        default=uuid.uuid4,
            editable=False
            )
    name = models.CharField(max_length=50)
    parentID = models.UUIDField(
    #        default=uuid.uuid4,
            editable=False,
            null=True
            )
    type = models.CharField(
            choices=ShopUnitType.choices,
            max_length=10)
    price = models.PositiveIntegerField(null=True)
    date = models.DateField()


class ShopUnitStatisticResponse(models.Model):
    items = models.ForeignKey(ShopUnitStatisticUnit, on_delete=models.CASCADE)


class Error(models.Model):
    code = models.PositiveIntegerField()
    message = models.TextField()

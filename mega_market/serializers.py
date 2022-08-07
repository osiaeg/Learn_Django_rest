from rest_framework import serializers
from .models import ShopUnit, ShopUnitType

class ShopUnitImportSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose')
    name = serializers.CharField()
    parentId = serializers.UUIDField(
            format='hex_verbose',
            allow_null=True,
            )
    type = serializers.CharField() # нужно узнать как проверять Enum
    price = serializers.IntegerField(allow_null=True)

    def validate_parentId(self, parent_id):
        """
        Check that parentID is category's id
        """
        if not parent_id is None:
            parent_type = ShopUnit.objects.get(pk=parent_id).type
            if parent_type == ShopUnitType.CATEGORY:
                return parent_id
            else:
                raise serializers.ValidationError("Parent ShopUnit isn't category")
        else:
            return parent_id


    def validate(self, data):
        """
        Category should have field price = null
        """
        if data['type'] == ShopUnitType.CATEGORY:
            if data['price'] is None:
                return data
            else:
                raise serializers.ValidationError("Category should have field pice = null")
        elif data['type'] == ShopUnitType.OFFER:
            if not data['price'] is None and data['price'] > 0:
                return data
            else:
                raise serializers.ValidationError("Offer price isn't correct")

    def create(self, validated_data):
        return ShopUnit.objects.create(**validated_data)


class ShopUnitImportRequestSerializer(serializers.Serializer):
    items = serializers.ListField(
            allow_empty=False,
            child=ShopUnitImportSerializer()
            )
    updateDate = serializers.DateTimeField()

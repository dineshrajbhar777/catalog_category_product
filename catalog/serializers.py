from rest_framework import serializers
#from rest_framework.response import Response
from .models import Category, Product
           
class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CategorySerializers(serializers.ModelSerializer):
    childcategories = RecursiveSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'childcategories',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'categories')

#class CategorySerializers(serializers.ModelSerializer):
#    class Meta:
#        model = Category
#        fields = ('id', 'name', 'parent')

    #def get_fields(self):
    #    fields = super(CategorySerializers, self).get_fields()
    #    #fields['childcategories'] = CategorySerializers(many=True, allow_null=True)
    #    return fields


#class CategorySerializers(serializers.ModelSerializer):
#    class Meta:
#        model = Category
#        fields = ('id', 'name', 'parent')
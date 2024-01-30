from rest_framework import serializers
from .models import Category, Product
from rest_framework.reverse import reverse
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = (
            'title',
            'category',
            'description',
            'price',
            'quantity',
            'cover'
        )
        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = "__all__"
        
    def get_products(self, obj):
        request = self.context['request']
        products = Product.objects.filter(category=obj)
        return [{"name": product.title ,"link": reverse('product-detail', args=[product.id], request=request)} for product in products]
    
    def get_object(self, view_name, view_args, view_kwargs):
        view_kwargs['category'] = str(view_kwargs['category'])
        return super().get_object(view_name, view_args, view_kwargs)
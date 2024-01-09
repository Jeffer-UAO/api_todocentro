from rest_framework.serializers import ModelSerializer
from products.models import Gallery, Category, Product, CategoryProduct, Attribut, AttributProduct






class ProductSerializer(ModelSerializer):
    # atributData = AttributSerializer(source='atribut', read_only=True, many=True)
    class Meta:
        model = Product
        fields = [
            "codigo",
            "ref",
            "flag",
            "name_extend",
            "slug",
            "description",          
            "images",
            "video_url",
            "image_alterna",
            "price_old",
            "price1",
            "qty",
            "price2",
            "active",
            "soldout",
            "offer",
            "home",       
        ]

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "codigo", "name", "slug", "image", "image_alterna"]

class CategoryProductSerializer(ModelSerializer):
    categoryData = CategorySerializer(source="category", read_only=True)
    productData = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = CategoryProduct
        fields = ["id", "active", "productData", "categoryData"]

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["id", "product", "image", "image_alterna",]

class AttributSerializer(ModelSerializer):
    class Meta:
        model = Attribut
        fields = ["id", "name"]

class AttributeProductSerializer(ModelSerializer):
    dataAttribute = AttributSerializer(source="attribut", read_only=True)
    dataProduct = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = CategoryProduct
        fields = ["dataAttribute", "dataProduct"]
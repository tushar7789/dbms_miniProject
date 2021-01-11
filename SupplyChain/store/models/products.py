from django.db import models
from .categories import Category

class Product(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    Name = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=30)
    Price = models.BigIntegerField(default=0)
    Image = models.ImageField(upload_to='store/uploads/products')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_products_by_id(ids):
        #return Product.objects.filter(id__in = ids)
        sql = ''' select * from store_product where id=%s '''
        size = len(ids)
        if size:
            p = Product.objects.raw(sql, [ids[0]])

            for i in range(1, size):
                p1 = Product.objects.raw(sql, [ids[i]])
                p = p1.union(p) 
            
            return p
        zero = 0
        return Product.objects.raw(sql, [zero])

    @staticmethod
    def get_all_products():
        #return Product.objects.all()
        sql = ''' select * from store_product'''
        return Product.objects.raw(sql)
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
            #return Product.objects.filter(Category=category_id)
            sql = ''' select * from store_product where "Category_id"=%s '''
            return Product.objects.raw(sql, [category_id])
    
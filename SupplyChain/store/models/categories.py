from django.db import models

class Category(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    Name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        #return Category.objects.all()
        sql = ("select * from store_category")
        return Category.objects.raw(sql) 

    def __str__(self):
        return self.Name
 
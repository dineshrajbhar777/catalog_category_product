from django.db import models

class Category(models.Model):
    id     = models.AutoField(primary_key=True)
    name   = models.CharField(max_length=250, unique=True, blank=False, null=False)
    parent = models.ForeignKey("self", related_name= "childcategories", 
                blank=True, null=True, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Categories'
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Category_detail", kwargs={"pk": self.id})

class Product(models.Model):
    id         = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=250, unique=True, blank=False, null= False)
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        db_table = 'Product'
    
    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reversed("Product_detail", kwargs={"pk": self.id})
    
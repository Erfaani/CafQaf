from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(
        upload_to="category_icon/", default="category_icon/default.png"
    )

    def __str__(self):
        return str(self.name)
    
    @property
    def get_number_of_products(self):
        return Product.objects.filter(category=self).count()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    available = models.BooleanField(default=True)
    amount = models.IntegerField(verbose_name="تعداد")

    def __str__(self):
        return str(self.name)


class Table(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_available = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.name)

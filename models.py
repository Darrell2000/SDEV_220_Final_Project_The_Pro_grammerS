from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    FOOD_CHOICES = [
        ('Taco', 'Taco'),
        ('Supreme Taco', 'Supreme Taco'),
        ('Quesadilla', 'Quesadilla'),
        ('Burrito', 'Burrito'),
        ('Nachos', 'Nachos'),
        ('Arroz con Pollo', 'Arroz con Pollo'),
    ]

    MEAT_CHOICES = [
        ('Steak', 'Steak'),
        ('Chicken', 'Chicken'),
        ('Pastor', 'Pastor'),
        ('Chorizo', 'Chorizo'),
        ('Ground Beef', 'Ground Beef'),
    ]

    name = models.CharField(max_length=50, choices=FOOD_CHOICES)
    meat = models.CharField(max_length=50, choices=MEAT_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.meat})"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    timestamp = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"
    
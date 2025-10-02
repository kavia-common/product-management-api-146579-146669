from django.db import models


class Product(models.Model):
    """
    Product model representing an item in the inventory with basic attributes.
    """
    name = models.CharField(max_length=255, db_index=True, help_text="Human-readable product name.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product price in standard currency.")
    quantity = models.IntegerField(default=0, help_text="Available quantity in stock.")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the product was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the product was last updated.")

    class Meta:
        ordering = ["id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f"{self.name} (#{self.pk})"

from rest_framework import serializers
from .models import Product

# PUBLIC_INTERFACE
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model, used for API input/output validation.

    Fields:
    - id: Auto-generated primary key.
    - name: Required string field, max length 255.
    - price: Decimal with two decimal places.
    - quantity: Integer, non-negative.
    """
    id = serializers.IntegerField(read_only=True, help_text="Auto-generated unique identifier for the product.")

    # PUBLIC_INTERFACE
    class Meta:
        model = Product
        fields = ("id", "name", "price", "quantity", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")

    def validate_quantity(self, value):
        """Ensure quantity is not negative."""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    def validate_price(self, value):
        """Ensure price is not negative."""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

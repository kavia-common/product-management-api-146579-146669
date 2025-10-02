from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product


class ProductApiTests(APITestCase):
    def setUp(self):
        self.list_url = reverse('product-list-create')

    def test_create_list_retrieve_update_delete_product(self):
        # Create
        payload = {"name": "Widget", "price": "12.34", "quantity": 5}
        resp = self.client.post(self.list_url, data=payload, format="json")
        self.assertEqual(resp.status_code, 201, resp.data)
        product_id = resp.data["id"]

        # List
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(any(p["id"] == product_id for p in resp.data.get("results", resp.data)))

        # Retrieve
        detail_url = reverse('product-detail', kwargs={"id": product_id})
        resp = self.client.get(detail_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["name"], "Widget")

        # Update
        update = {"name": "Widget Pro", "price": "15.00", "quantity": 7}
        resp = self.client.put(detail_url, data=update, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["name"], "Widget Pro")

        # Delete
        resp = self.client.delete(detail_url)
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Product.objects.filter(id=product_id).exists())

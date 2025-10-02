from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from drf_yasg.utils import swagger_auto_schema

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def health(request):
    """
    Simple health check endpoint.
    """
    return Response({"message": "Server is up!"})


class OceanBrowsableAPIRenderer(BrowsableAPIRenderer):
    """
    Custom Browsable API Renderer to reflect 'Ocean Professional' theme accents.
    Applies subtle blue and amber accents using inline CSS for the browsable UI.
    """
    # Inject light custom styles in the header
    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)
        context['styles'] = (
            context.get('styles', '') +
            """
            <style>
              :root {
                --ocean-primary: #2563EB;
                --ocean-secondary: #F59E0B;
                --ocean-text: #111827;
                --ocean-surface: #ffffff;
                --ocean-bg: #f9fafb;
              }
              body { background: var(--ocean-bg); color: var(--ocean-text); }
              .navbar, .breadcrumb { background: var(--ocean-surface); box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
              .btn-primary, .button { background: var(--ocean-primary) !important; border-color: var(--ocean-primary) !important; }
              a { color: var(--ocean-primary); }
              .btn-info { background: var(--ocean-secondary) !important; border-color: var(--ocean-secondary) !important; color: #1f2937 !important; }
              code, pre { border-radius: 6px; }
              .highlight { border-radius: 8px; }
              .form-control, select { border-radius: 6px !important; }
              .page-header h1, h2, h3 { color: var(--ocean-primary); }
              .well { border-left: 4px solid var(--ocean-secondary); }
            </style>
            """
        )
        return context


# PUBLIC_INTERFACE
class ProductListCreateView(generics.ListCreateAPIView):
    """
    REST endpoint to list all products and create a new product.

    GET /api/products/:
        Returns a paginated list of products.
    POST /api/products/:
        Creates a new product with fields: name, price, quantity.

    Responses:
        200 OK (list), 201 Created (create), 400 Bad Request (validation error).
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer, OceanBrowsableAPIRenderer]

    @swagger_auto_schema(
        operation_id="listProducts",
        operation_summary="List products",
        operation_description="Retrieve a list of products with id, name, price, and quantity.",
        responses={200: ProductSerializer(many=True)},
        tags=["Products"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="createProduct",
        operation_summary="Create product",
        operation_description="Create a new product by providing name, price, and quantity.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Validation Error"},
        tags=["Products"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# PUBLIC_INTERFACE
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    REST endpoint to retrieve, update, or delete a specific product.

    GET /api/products/{id}/:
        Retrieve a product by id.
    PUT /api/products/{id}/:
        Update all fields of a product.
    DELETE /api/products/{id}/:
        Delete a product by id.

    Responses:
        200 OK, 204 No Content (delete), 400 Bad Request, 404 Not Found.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer, OceanBrowsableAPIRenderer]
    lookup_field = "id"

    @swagger_auto_schema(
        operation_id="getProduct",
        operation_summary="Retrieve product",
        operation_description="Retrieve a single product by id.",
        responses={200: ProductSerializer, 404: "Not Found"},
        tags=["Products"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="updateProduct",
        operation_summary="Update product",
        operation_description="Update a product by id with name, price, and quantity.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 400: "Validation Error", 404: "Not Found"},
        tags=["Products"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="deleteProduct",
        operation_summary="Delete product",
        operation_description="Delete a product by id.",
        responses={204: "No Content", 404: "Not Found"},
        tags=["Products"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

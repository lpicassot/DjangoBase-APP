from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

from .handlers.helpers import WordFinder


class ProductView(APIView):
    """
    A Product Vew for listing or creating products.
    """
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


    def put(self, request):
        serializer = ProductSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():            
            serializer.save()
            # Return the serialized new instance in the response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors in the response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# Save the new instance
        

class SearchCoordsView(APIView):
    def get(self, request, format=None):
        product_name = request.query_params.get('product')
        print(product_name)
        
        # Create list of all products names
        all_product_names = list(Product.objects.values_list('name', flat=True))
        print(all_product_names)

        # Execute longest_word_finder
        w = WordFinder()
        filtered_products_name = w.longest_word(all_product_names, product_name)

        # Filter Product Objects
        filtered_products = Product.objects.filter(name__in=filtered_products_name)
        if filtered_products.count() > 0:
            # Serialize vlaue
            serializer = ProductSerializer(filtered_products, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response({"Error": "No Products Available"}, status.HTTP_404_NOT_FOUND)
            




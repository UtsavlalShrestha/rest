from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Product, ProductType, Department, Purchase, vendors, Sell
from .serializers import ProductSerializer, ProductTypeSerializer, DepartmentSerializer, PurchaseSerializer,SellSerializer,VendorSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  #object to json format also does data validation as well

class ProductTypeApiView(GenericAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def get(self, request):
        product_type_objs = self.get_queryset()  #gets values from queryset
        serializer = self.get_serializer(product_type_objs, many=True)  #created serializer object
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)  #here obj not passed but data that is be created is passed for json change as well as validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductTypeDetailApiView(GenericAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def get(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        product_type_obj = self.get_object()
        serializer = self.get_serializer(product_type_obj, data=request.data)  #data is kun naya data leh update garne
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        product_type_obj = self.get_object()
        product_type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DepartmentApiView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request):
        dept_obj = self.get_queryset()
        serializer = self.get_serializer(dept_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DepartmentTypeApiView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, pk):
        dept_type_obj = self.get_object()
        serializer = self.get_serializer(dept_type_obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        dept_type_obj = self.get_object()
        serializer = self.get_serializer(dept_type_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        dept_type_obj = self.get_object()
        dept_type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PurchaseApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self, request):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PurchaseDetailApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self, request, pk):
        purchase_obj = self.get_object()
        serializer = self.get_serializer(purchase_obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        purchase_obj = self.get_object()
        serializer = self.get_serializer(purchase_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        purchase_obj = self.get_object()
        purchase_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SellApiView(GenericAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    def get(self, request):
        sell_obj = self.get_queryset()
        serializer = self.get_serializer(sell_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SellDetailApiView(GenericAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    def get(self, request, pk):
        sell_obj = self.get_object()
        serializer = self.get_serializer(sell_obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sell_obj = self.get_object()
        serializer = self.get_serializer(sell_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        sell_obj = self.get_object()
        sell_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class VendorApiView(GenericAPIView):
    queryset = vendors.objects.all()
    serializer_class = VendorSerializer

    def get(self, request):
        vendor_obj = self.get_queryset()
        serializer = self.get_serializer(vendor_obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class VendorDetailApiView(GenericAPIView):
    queryset = vendors.objects.all()
    serializer_class = VendorSerializer

    def get(self, request, pk):
        vendor_obj = self.get_object()
        serializer = self.get_serializer(vendor_obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        vendor_obj = self.get_object()
        serializer = self.get_serializer(vendor_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        vendor_obj = self.get_object()
        vendor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


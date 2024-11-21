from django.contrib import admin
from django.urls import path
from base.views import ProductApiView, ProductTypeApiView, ProductTypeDetailApiView, DepartmentApiView, DepartmentTypeApiView, PurchaseApiView,PurchaseDetailApiView, VendorApiView, VendorDetailApiView, SellApiView, SellDetailApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductApiView.as_view({'get': 'list', 'post':'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get': 'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    path('product-type/', ProductTypeApiView.as_view()),
    path('product-type/<int:pk>/', ProductTypeDetailApiView.as_view()),
    path('department/', DepartmentApiView.as_view()),
    path('department/<int:pk>/', DepartmentTypeApiView.as_view()),
    path('purchase/', PurchaseApiView.as_view()),
    path('purchase/<int:pk>/', PurchaseDetailApiView.as_view()),
    path('vendor/', VendorApiView.as_view()),
    path('vendor/<int:pk>/', VendorDetailApiView.as_view()),
    path('sell/', SellApiView.as_view()),
    path('sell/<int:pk>/', SellDetailApiView.as_view()),



]

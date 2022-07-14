
from django.urls import path, reverse_lazy

# from .views import PosHome
from rest_api.barcode_api.views import BarcodeAPIView, BarcodeDetailAPIView
from rest_api.category_api.views import CategoryAPIView, CategoryDetailAPIView
from rest_api.qr_code_api.views import QrCodeAPIView, QrCodeDetailAPIView
from rest_api.invoice_api.views import InvoiceAPIView, InvoiceDetailAPIView
# from rest_api.customer_api.views import CustomerAPIView, CustomerDetailAPIView
from rest_api.category_product_api.views import CategoryProductAPIView, CategoryProductDetailAPIView
from rest_api.expense_api.views import ExpenseAPIView, ExpenseDetailAPIView
from rest_api.notification_api.views import NotificationAPIView, NotificationDetailAPIView
from rest_api.pos_order_api.views import PosOrderAPIView, PosOrderDetailAPIView
from rest_api.product_api.views import ProductAPIView, ProductDetailAPIView
from rest_api.product_variant_option_api.views import ProductVariantOptionAPIView, ProductVariantOptionDetailAPIView
from rest_api.shopping_cart_api.views import ShoppingCartAPIView, ShoppingCartDetailAPIView
from rest_api.selected_product_variant_api.views import SelectedProductVariantAPIView, SelectedProductVariantDetailAPIView
from rest_api.session_api.views import SessionAPIView, SessionDetailAPIView
from rest_api.shopping_cart_product_api.views import ShoppingCartProductAPIView, ShoppingCartProductDetailAPIView
# from rest_api.shopping_cart_product_variant_api.views import ShoppingCartProductVariantAPIView, ShoppingCartProductVariantDetailAPIView
from rest_api.variant_api.views import VariantAPIView, VariantDetailAPIView
from rest_api.variant_option_api.views import VariantOptionAPIView, VariantOptionDetailAPIView
from rest_api.variant_product_api.views import VariantProductAPIView, VariantProductDetailAPIView
# New Models
from rest_api.logs_api.views import LogsAPIView, LogsDetailAPIView
from rest_api.product_log_api.views import ProductLogAPIView, ProductLogDetailAPIView


app_name = "rest_api"


urlpatterns = [
     # barcode_api
     path('barcode/', BarcodeAPIView.as_view(), name="barcode_list"),
     path('barcode/<int:barcode_pk>/', BarcodeDetailAPIView.as_view(), name="barcode_detail"),

     # qr_code_api
     path('qr_code/', QrCodeAPIView.as_view(), name="qr_code_list"),
     path('qr_code/<int:qr_code_pk>/', QrCodeDetailAPIView.as_view(), name="qr_code_detail"),

     # invoice_api
     path('invoice/', InvoiceAPIView.as_view(), name="invoice_list"),
     path('invoice/<int:invoice_pk>/', InvoiceDetailAPIView.as_view(), name="invoice_detail"),

     # category_product_api
     path('category_product/', CategoryProductAPIView.as_view(), name="category_product_list"),
     path('category_product/<int:category_product_pk>/', CategoryProductDetailAPIView.as_view(), name="category_product_detail"),

     # category_api
     path('category/', CategoryAPIView.as_view(), name="category_list"),
     path('category/<int:category_pk>/', CategoryDetailAPIView.as_view(), name="category_detail"),
     
     # expense_api
     path('expense/', ExpenseAPIView.as_view(), name="expense_list"),
     path('expense/<int:expense_pk>/', ExpenseDetailAPIView.as_view(), name="expense_detail"),
     
     # notiicaiton_api
     path('notification/', NotificationAPIView.as_view(), name="notification_list"),
     path('notification/<int:notification_pk>/', NotificationDetailAPIView.as_view(), name="notification_detail"),
     
     # pos_order_api
     path('order/', PosOrderAPIView.as_view(), name="pos_order_list"),
     path('order/<int:pos_order_pk>/', PosOrderDetailAPIView.as_view(), name="pos_order_detail"),
     
     # product_api
     path('product/', ProductAPIView.as_view(), name="product_list"),
     path('product/<int:product_pk>/', ProductDetailAPIView.as_view(), name="product_detail"),

     # product_variant_option_api
     path('product_variant_option/', ProductVariantOptionAPIView.as_view(), name="product_variant_option_list"),
     path('product_variant_option/<int:product_variant_option_pk>/', ProductVariantOptionDetailAPIView.as_view(), name="product_variant_option_detail"),

     # shopping_cart_api
     path('shopping_cart/', ShoppingCartAPIView.as_view(), name="shopping_cart_list"),
     path('shopping_cart/<int:shopping_cart_pk>/', ShoppingCartDetailAPIView.as_view(), name="shopping_cart_detail"),

     # product_variant_option_api
     path('selected_product_variant/', SelectedProductVariantAPIView.as_view(), name="selected_product_variant_list"),
     path('selected_product_variant/<int:selected_product_variant_pk>/', SelectedProductVariantDetailAPIView.as_view(), name="selected_product_variant_detail"),
     
     # session_api
     path('session/', SessionAPIView.as_view(), name="session_list"),
     path('session/<int:session_pk>/', SessionDetailAPIView.as_view(), name="session_detail"),
     
     # shopping_cart_api
     path('shopping_cart_product/', ShoppingCartProductAPIView.as_view(), name="shopping_cart_product_list"),
     path('shopping_cart_product/<int:shopping_cart_product_pk>/', ShoppingCartProductDetailAPIView.as_view(), name="shopping_cart_product_detail"),
     
     # variant_api
     path('variant/', VariantAPIView.as_view(), name="shopping_cart_product_variant_list"),
     path('variant/<int:variant_pk>/', VariantDetailAPIView.as_view(), name="shopping_cart_product_variant_detail"),
     
     # variant_option_api
     path('variant_option/', VariantOptionAPIView.as_view(), name="shopping_cart_product_variant_list"),
     path('variant_option/<int:variant_option_pk>/', VariantOptionDetailAPIView.as_view(), name="shopping_cart_product_variant_detail"),
     
     # variant_product_api
     path('variant_product/', VariantProductAPIView.as_view(), name="shopping_cart_product_variant_list"),
     path('variant_product/<int:variant_product_pk>/', VariantProductDetailAPIView.as_view(), name="shopping_cart_product_variant_detail"),
     
     # log_api
     path('log/', LogsAPIView.as_view(), name="log_list"),
     path('log/<int:log_pk>/', LogsDetailAPIView.as_view(), name="log_detail"),
     
     # product_log_api
     path('product_log/', ProductLogAPIView.as_view(), name="product_log_list"),
     path('product_log/<int:product_log_pk>/', ProductLogDetailAPIView.as_view(), name="product_log_detail"),
     
]




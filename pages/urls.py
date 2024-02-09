from django.urls import path
from .views import HomeTempleView, ProductListView,ProductDetailView
app_name = "pages"


urlpatterns = [
    path("",HomeTempleView.as_view(),name='home'),
    path("men-shoes/",ProductListView.as_view(),name="products"),
    path("order-shoes/<str:pk>",ProductDetailView.as_view(),name="product")
]
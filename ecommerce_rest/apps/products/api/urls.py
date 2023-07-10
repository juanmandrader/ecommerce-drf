from django.urls import path
from apps.products.api.views.general_views import (
    MeasureUnitListAPIView,
    IndicatorSerializerListAPIView,
    CategoryProductSerializerListAPIView
)
from apps.products.api.views.products_view import ProductListAPIView

urlpatterns = [
    path(
        'measure_unit/',
        MeasureUnitListAPIView.as_view(),
        name="measure_unit"
    ),
    path(
        'indicator/',
        IndicatorSerializerListAPIView.as_view(),
        name="indicator"
    ),
    path(
        'category_product/',
        CategoryProductSerializerListAPIView.as_view(),
        name="category_product"
    ),
    path(
        'product/',
        ProductListAPIView.as_view(),
        name="product"
    )
]


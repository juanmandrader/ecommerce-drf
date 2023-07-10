from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer,
    IndicatorSerializer,
    CategoryProductSerializer
)
    
class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
    

class IndicatorSerializerListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer


class CategoryProductSerializerListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer

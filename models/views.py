from LiftData import LiftData
from serializers import LiftDataSerializer
from commons.views.BaseView import BaseRetrieveView, BaseListView, BaseListCreateView

class LiftDataView(BaseRetrieveView):
    model = LiftData
    serializer_class = LiftDataSerializer
    depth = 3

class LiftDataListView(BaseListCreateView):
    model = LiftData
    serializer_class = LiftDataSerializer

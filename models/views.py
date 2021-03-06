from models import LiftData, LiftHistory, LiftSet
from serializers import LiftDataSerializer, LiftHistorySerializer, LiftSetSerializer
from commons.views.BaseView import BaseRetrieveView, BaseListView, BaseCreateView, BaseListCreateView, BaseRetrieveUpdateDestroyView
from rest_framework.response import Response
from managers.LiftDataManager import LiftDataManager

class LiftDataView(BaseRetrieveView):
    model = LiftData
    serializer_class = LiftDataSerializer
    depth = 3

class LiftDataListCreateView(BaseListCreateView):
    model = LiftData
    serializer_class = LiftDataSerializer

class LiftDataRetrieveUpdateDestroy(BaseRetrieveUpdateDestroyView):
    model = LiftData
    serializer_class = LiftDataSerializer
        
class LiftDataSearchView(BaseListView):
    model = LiftData
    serializer_class = LiftDataSerializer

    def get(self, request, **kwargs):
        print (kwargs);
        requestingUserId = request.user.id
        searchFilter = LiftDataManager.generateLiftDataSearchFilter(kwargs)
        notes = LiftDataManager.searchLiftData(requestingUserId, searchFilter)
        serializer = self.serializer_class(notes)
        return Response(serializer.data)

class LiftHistoryListCreateView(BaseListCreateView):
    model = LiftHistory
    serializer_class = LiftHistorySerializer
    
class LiftSetListCreateView(BaseListCreateView):
    model = LiftSet
    serializer_class = LiftSetSerializer
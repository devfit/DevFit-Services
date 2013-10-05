from models.models import LiftData
from models.serializers import LiftDataSerializer
from commons.utils.Global import URL_PARAM_SEPARATOR, DEFAULT_SORT, DEFAULT_ROW_COUNT
from django.db.models.aggregates import Count
from filters.LiftDataFilter import LiftDataFilter

class LiftDataManager():
    
    @staticmethod
    def getParamsFromUrl(urlParams):
        f = {}
        # Basic Filters
        f['s'] = urlParams.get('s', None)
        f['offset'] = urlParams.get('offset', 0)
        f['rowcount'] = urlParams.get('rowcount', DEFAULT_ROW_COUNT)
        f['sort'] = urlParams.get('sort', "")
        f['format'] = urlParams.get('format', None)
        
        # BL Filters
        f['user'] = urlParams.get('user', None)

        return f
    
    @staticmethod
    def generateLiftDataSearchFilter(urlParams):
        f = LiftDataManager.getParamsFromUrl(urlParams)

        sortFields = [DEFAULT_SORT]
        if f['sort']:
            sortFields = [str(x) for x in f['sort'].split(URL_PARAM_SEPARATOR)]
            
        searchFilter = LiftDataFilter()
        searchFilter.set_search_key(f['s'])
        searchFilter.set_sort(sortFields)
        searchFilter.set_offset(f['offset'])
        searchFilter.set_rowcount(f['rowcount'])
        
        searchFilter.set_user(f['user'])
        
        return searchFilter
    
    @staticmethod
    def searchLiftData(requestinUserId, searchFilter):
        print(searchFilter.set_search_key);
    

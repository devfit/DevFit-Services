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
        # Generate filter string
        filterString = ""
        searchKey = searchFilter.get_search_key()
        if searchKey is not None:
            filterString += ".filter(note__icontains=searchKey)"
#            filterString += ".filter(Q(headline__icontains=searchKey) | Q(note_description__icontains=searchKey))"
        
        noteTypes = searchFilter.get_note_types()
        if noteTypes:
            filterString += ".filter(note_type__in=noteTypes)"
        
        start_date = searchFilter.get_start_date()
        if start_date:
            filterString += ".filter(calendar_entries__start_date__gte=start_date)"
            
        end_date = searchFilter.get_end_date()
        if end_date:
            filterString += ".filter(calendar_entries__end_date__lte=end_date)"
        
        filterList = BLManager.getCommonCoreFilterList(searchFilter)
        if filterList:
            filterString += ".extra(where=filterList)"
            
        # Paging and Sorting
        offset = int(searchFilter.get_offset())
        toRow = offset + int(searchFilter.get_rowcount())
        sort = searchFilter.get_sort()
        # Evaluate and return values
        
        noteQueryString = "BLNote.objects" + filterString + ".distinct().order_by(*sort)[offset:toRow]"
        notes = eval(noteQueryString)
        return notes
    

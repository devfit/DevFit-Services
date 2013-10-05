from commons.utils.Global import DEFAULT_ROW_COUNT, DEFAULT_SORT

class LiftDataFilter():
    
    def __init__(self):
        self.__searchKey = None
        self.__offset = 0
        self.__rowcount = DEFAULT_ROW_COUNT
        self.__sort = [DEFAULT_SORT]
        self.__user = None


    def get_search_key(self):
        return self.__searchKey


    def get_offset(self):
        return self.__offset


    def get_rowcount(self):
        return self.__rowcount


    def get_sort(self):
        return self.__sort
    
    
    def get_user(self):
        return self.__user


    def set_search_key(self, value):
        self.__searchKey = value


    def set_offset(self, value):
        self.__offset = value


    def set_rowcount(self, value):
        self.__rowcount = value


    def set_sort(self, value):
        self.__sort = value
        
        
    def set_user(self, value):
        self.__user = value


    def del_search_key(self):
        del self.__searchKey


    def del_offset(self):
        del self.__offset


    def del_rowcount(self):
        del self.__rowcount


    def del_sort(self):
        del self.__sort
        
    def del_user(self):
        del self.__user
        
    searchKey = property(get_search_key, set_search_key, del_search_key, "searchKey's docstring")
    offset = property(get_offset, set_offset, del_offset, "offset's docstring")
    rowcount = property(get_rowcount, set_rowcount, del_rowcount, "rowcount's docstring")
    sort = property(get_sort, set_sort, del_sort, "sort's docstring")
    
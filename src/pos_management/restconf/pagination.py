from rest_framework import pagination



class PosPagination(pagination.LimitOffsetPagination): #PageNumberPagination):
    # page_size   =  1000
    default_limit   = 5
    max_limit       = 10
    #limit_query_param = 'lim' 

from rest_framework import generics, authentication
from rest_framework.renderers import JSONRenderer, JSONPRenderer, \
    BrowsableAPIRenderer

AUTHENTICATION_CLASSES = (authentication.TokenAuthentication, authentication.SessionAuthentication,)
RENDERER_CLASSES = (JSONRenderer, JSONPRenderer, BrowsableAPIRenderer)

class BaseListView(generics.ListAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES

class BaseRetrieveView(generics.RetrieveAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES
    
class BaseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES

class BaseCreateView(generics.CreateAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES

class BaseListCreateView(generics.ListCreateAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES
    
class BaseRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES

class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = AUTHENTICATION_CLASSES
    renderer_classes = RENDERER_CLASSES



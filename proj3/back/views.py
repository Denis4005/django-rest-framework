from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import *
from rest_framework.pagination import PageNumberPagination

from .models import Car
from .serializers import CarSerializer


class CarAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CarAPIListPagination

class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly, )





# class CarViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = CarSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Car.objects.all()[:3]
#         else:
#             return Car.objects.filter(pk=pk)

#     @action(methods=['get'], detail = True)
#     def category(self,request,pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats':cats.name})



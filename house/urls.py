from django.urls import path
from house.views import HouseListView, NewHouseView, HouseDetail, HouseDeleteView, HouseUpdateView

urlpatterns = [
    path('house/', HouseListView.as_view(), name='house_list'),
    path('new_house/', NewHouseView.as_view(), name='new_house'),
    path('house_detail/<uuid:pk>/', HouseDetail.as_view(), name='house_detail'),
    path('house/<uuid:pk>/update', HouseUpdateView.as_view(), name='house_update'),
    path('house/<uuid:pk>/delete', HouseDeleteView.as_view(), name='house_delete'),
]
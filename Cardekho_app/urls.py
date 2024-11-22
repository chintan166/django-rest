from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('showroom',views.Showroom_Viewset,basename='showroom')

urlpatterns=[
    path('list',views.car_list_view,name="car_list"),
    path('<int:pk>',views.car_detail_view,name="car_detail"),
   # path('showroom',views.Showroom_view.as_view()),
   # path('showroom/<int:pk>',views.Showroom_detail.as_view(),name="Showroom_detail")
   path('',include(router.urls)),
]
from django.urls import path

from cats.views import APICat, APICatDetail, CatList, CatDetail

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view())

]



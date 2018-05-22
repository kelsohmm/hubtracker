from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:year>/<int:month>/<int:day>', views.date_view, name='index'),
]
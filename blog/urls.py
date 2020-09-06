from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',   # <>-извлечение значений из urla, возвращается в виде строки
         views.post_detail, name='post_detail')
]
#Первый шаблон не принимает никаких аргументов. Он сопоставляется с обработчиком
#post_list. Второй вызывает функцию post_detail и принимает в качестве параметров
#год, месяц, день публикации + строку которая может содержать буквы, цыфры, дефисы, нижние подчеркивания.














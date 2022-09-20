from django.urls import path
from . import views
urlpatterns = [
  path('',views.index),
  path('login/',views.login),
  path('table/',views.table),
  path('welcome/',views.welcome),
  path('formdata/',views.form_data,name='reform'),
  path('login_data/',views.Login_form,name='form'),
  path('data/',views.data,name='alldata'),
  path('delete_user/',views.delete_user)


]
from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static
from userregister import views as ac_views
from website.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', views.index, name='home'),
                  path('login', ac_views.login, name='login'),
                #   path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
                  path('register', ac_views.register, name='register'),
                  path('cat/<int:pk>', cat, name='cat'),
                  path('them/<int:pk>/<int:bi>', them_cat, name='them_cat'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

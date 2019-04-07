

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from .views import home_page
from faculty.views import facultyinfo
from table.views import Timetable_view
from accounts.views import Login_View,Admin_Login_View,FRegister_View,ARegister_View,Admin_home,Faculty_home,Logout_view

urlpatterns = [

    url(r'^info/$', facultyinfo,name='facultyinfo'),
    url(r'^login/$', Login_View,name='login'),
    url(r'^fregis/$', FRegister_View,name='faculty_register'),
    url(r'^aregis/$', ARegister_View,name='admin_register'),
    url(r'^adminpage/$', Admin_Login_View,name='admin'),
    url(r'^admin_home/$', Admin_home,name='admin_home'),
    url(r'^logout/$', Logout_view, name='logout'),
    url(r'^time_table/$', Timetable_view, name='time_table'),
    url(r'^faculty_home/$', Faculty_home,name='faculty_home'),


    url(r'^$', home_page,name='home'),
    url(r'^admin/', admin.site.urls),
]


if  settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

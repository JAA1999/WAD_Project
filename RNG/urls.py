
from django.conf.urls import url, include
from RNG import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/', views.category, name='category'),
    url(r'^signup/$', views.signup, name='signup'),
	url(r'^signin/$', views.user_login, name='signin'),
	url(r'^signout/$', views.user_logout, name='signout'),
    url(r'^game', views.signup, name='game'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url
from RNG import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/$', views.show_categories, name='show_categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<game_name_slug>[\w\-]+)/$', views.game, name='game'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_game/$', views.add_game, name='add_game'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.user_login, name='signin'),
    url(r'^signout/$', views.user_logout, name='signout'),
    #url(r'^game', views.game, name='game'),
    #url(r'^search', views.search, name='search'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

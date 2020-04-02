from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from users import views
from communication.views import mailme, successView

urlpatterns =  [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    #    path('update/<int:id>', views.updateUser, name='update'),
    path('update/', views.updateUser, name='update'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('mailme/<user_to>/', mailme),
    path('success/', successView, name='success'), prefix_default_language=False
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns

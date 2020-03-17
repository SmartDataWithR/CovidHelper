from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from users import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('update/<int:id>', views.updateUser, name='update'),
    path('update/', views.updateUser, name='update'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns

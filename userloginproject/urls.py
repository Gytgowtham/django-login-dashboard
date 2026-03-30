from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 LOGIN / LOGOUT URLs
    path('accounts/', include('django.contrib.auth.urls')),

    # 👇 USERS APP
    path('', include('users.urls')),
]

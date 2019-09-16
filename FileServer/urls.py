
from django.contrib import admin
from django.urls import path, include

import accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include(accounts.urls)),
]

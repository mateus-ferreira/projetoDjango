from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('biblioteca.urls')),
	path('blog/', include('blog.urls')),
	path('accounts/', include('users.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
]
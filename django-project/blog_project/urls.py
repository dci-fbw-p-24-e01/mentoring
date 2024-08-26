
from django.contrib import admin
from django.urls import path, include

# from blog import views as blog_views
# from todo import views as todo_views

from blog.views import home

urlpatterns = [
    # path('', views.home, name='home'),
    # path('', blog_views.home, name='home'),
    
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]

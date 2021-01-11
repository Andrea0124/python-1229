from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, globalviews, showpost, WatchTWchart, Watchchart, showwatch, ViewsInTaiwan, showwatchTW


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('globalviews/', globalviews),
    path('watch/<str:slug>/', showwatch),
    path('viewsInTaiwan/', ViewsInTaiwan),
    path('watchTW/<str:slug>/', showwatchTW),
    path('Watchchart/', Watchchart),
    path('WatchTWchart/', WatchTWchart),
    path('', homepage),
]

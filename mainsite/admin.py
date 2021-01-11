from django.contrib import admin
from mainsite.models import Post, Watch, AccessInfo, WatchTW

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)

class WatchAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Watch, WatchAdmin)

class WatchTWAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(WatchTW, WatchTWAdmin)
admin.site.register(AccessInfo)
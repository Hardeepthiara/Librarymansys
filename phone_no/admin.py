from django.contrib import admin
from phone_no.models import*

# Register your models here.
admin.site.register(sep)

class MnoAdmin(admin.ModelAdmin):
	list_display=('name','bio',)
	fieldsets=(
		("Gereneral info",{
			"fields":("name","bio",)			}),
		("social media",{
			"classes":("collapse",),
			"fields":("twitter","facebook",),
			"description":"Add social meadia here"
			}))

admin.site.register(mno,MnoAdmin)


class trackAdmin(admin.ModelAdmin):
	list_display=('name',)

	search_fields=['name','abstract']
	list_filter=('name','abstract',)
admin.site.register(track,trackAdmin)
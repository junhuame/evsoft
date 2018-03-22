from django.contrib import admin
from .models import Area, Device, IpInif


admin.site.empty_value_display = '-未填写-'


class DeviceAdmin(admin.ModelAdmin):
    """设备管理"""
    list_display = ('name', 'remark')

class AreaAdmin(admin.ModelAdmin):
    """位置区域管理"""
    list_display=('name', 'remark')



class IpInifAdmin(admin.ModelAdmin):
    """位置区域管理"""
    def area_seat(self,obj):
        return f'{obj.area}{obj.seat}'


    list_display=('computer_name', 'ipad','openeye','area_seat','user')
    list_filter = ('area',)
    search_fields =['ipad','openeye','seat','seat']
    list_per_page = 20


admin.site.register(Device, DeviceAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(IpInif, IpInifAdmin)
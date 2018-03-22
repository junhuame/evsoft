from django.db import models



class Device(models.Model):
    """设备信息表"""
    name = models.CharField('型号',max_length=100)
    cpu = models.CharField('CPU', max_length=20,null=True,blank=True)
    RAM = models.CharField('内存', max_length=20,null=True,blank=True)
    remark = models.TextField('备注',null=True, blank=True)

    class Meta:
        ordering= ['name']
    
    def __str__(self):
        return self.name

class Area(models.Model):
    """所属位置区域表"""
    name = models.CharField('区域', max_length=50)
    remark = models.TextField('备注', null=True,blank=True)

    class Meta:
        ordering= ['name']

    def __str__(self):
        return self.name
    

class IpInif(models.Model):
    """ip信息类"""
    computer_name  = models.CharField('计算机名', max_length=30)
    device = models.ForeignKey('Device', on_delete=models.SET_NULL, null=True, related_name='ipinfos')
    ipad = models.GenericIPAddressField('IP地址', protocol='IPv4')
    macad = models.CharField('MAC地址', max_length=18, null=True,blank=True)
    openeye = models.IntegerField('OpenEye号', null=True,blank=True)
    area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True, related_name='ipinfos')
    seat = models.CharField('位置', max_length=50)
    user = models.CharField('使用人', max_length=20, default='不固定')
    updated = models.DateTimeField('最后更新', auto_now=True)
    remark = models.TextField('备注',null=True,blank=True)

    class Meta:
        ordering= ['area', 'seat']

    def __str__(self):
        return f'{self.ipad} - {self.area.name} {self.seat}'



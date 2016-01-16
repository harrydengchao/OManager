from django.db import models

# Create your models here.
class ServerFunCateg(models.Model):
    """docstring for ServerFunCateg"""
    server_categ_name = models.CharField(max_length = 60)
    delmark = models.CharField(max_length = 10, default = False)
    def __unicode__(self):
        return self.server_categ_name

class ServerAppCateg(models.Model):
    """docstring for ServerAppCateg"""
    fun_categ_id = models.IntegerField()
    app_categ_name = models.CharField(max_length = 90)
    delmark = models.CharField(max_length = 10, default = False)
    def __unicode__(self):
        return self.app_categ_name

class ServerHostList(models.Model):
    """docstring for ServerHostList"""
    app_categ_id = models.IntegerField()
    host_name = models.CharField(max_length = 40, primary_key = True)
    host_wip = models.CharField(max_length = 50)
    host_nip = models.CharField(max_length = 50)
    host_os = models.CharField(max_length = 30)
    delmark = models.CharField(max_length = 10, default = False)
    def __unicode__(self):
        return self.host_name

class ModuleList(models.Model):
    """docstring for ModuleList"""
    module_name = models.CharField(max_length = 60)
    module_caption = models.CharField(max_length = 800)
    module_extend = models.CharField(max_length = 6000)
    delmark = models.CharField(max_length = 10, default = False)
    def __unicode__(self):
        return self.module_name
        
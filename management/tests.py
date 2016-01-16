from django.test import TestCase
# -----------------------------------
from management.models import ServerFunCateg, ServerAppCateg, ServerHostList, ModuleList

# Create your tests here.
class ServerFunCategTestCase(TestCase):
    """docstring for ServerFunCategTestCase"""
    def setUp(self):
        ServerFunCateg.objects.create(server_categ_name = "cache")
    def test_FunName(self):
        funname = ServerFunCateg.objects.get(server_categ_name = "cache")
        self.assertEqual(funname.server_categ_name, "cache")
        self.assertEqual(funname.delmark, "False")

class ServerAppCategTestCase(TestCase):
    """docstring for ServerAppCategTestCase"""
    def setUp(self):
        ServerAppCateg.objects.create(fun_categ_id = 1, app_categ_name = "redis")
    def test_AppName(self):
        appname = ServerAppCateg.objects.get(app_categ_name = "redis")
        self.assertEqual(appname.app_categ_name, "redis")
        self.assertEqual(appname.delmark, "False")
        
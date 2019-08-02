from django.test import TestCase
from apps.configs.models import Enviorment
from apps.configs.models import Application
from apps.configs.models import Configuration
from apps.configs.models import Setting

class EnviormentTest(TestCase):

    def setUp(self):
        
        Enviorment.objects.create(
            name="dev"
        )

        Enviorment.objects.create(
            name="prod"
        )

        Enviorment.objects.create(
            name="staging"
        )

    def test_get_enviorments(self):

        envs = Enviorment.objects.all()
        self.assertEqual(len(list(envs)), 3)

    def test_get_enviorment_by_name(self):
        dev_env = Enviorment.objects.get(name="dev")
        self.assertEqual(dev_env.name, "dev")

        prod_env = Enviorment.objects.get(name="prod")
        self.assertEqual(prod_env.name, "prod")

        staging_env = Enviorment.objects.get(name="staging")
        self.assertEqual(staging_env.name, "staging")


class ApplicationTest(TestCase):

    def setUp(self):
        
        Application.objects.create(
            name="config-server"
        )

    def test_get_application_by_name(self):
        
        app = Application.objects.get(name="config-server")    
        self.assertEqual(app.name, "config-server")
        self.assertEqual(app.active, True)

class ConfigurationTest(TestCase):

    def setUp(self):

        self.application = Application.objects.create(
            name="config-server"
        )

        self.enviorment = Enviorment.objects.create(
            name="dev"
        )

    def test_create_a_configuration(self):

        configuration = Configuration.objects.create(
            application = self.application,
            enviorment = self.enviorment,
            active = False
        )    

        confs = Configuration.objects.all()
        
        self.assertEqual(len(list(confs)), 1)
        conf_object = confs[0]

        self.assertEqual(conf_object.application.name, "config-server")
        self.assertEqual(conf_object.enviorment.name, "dev")
        self.assertEqual(conf_object.active, False)


class TestSetting(TestCase):

    def setUp(self):

        self.application = Application.objects.create(
            name="config-server"
        )

        self.enviorment = Enviorment.objects.create(
            name="dev"
        )

        self.configuration = Configuration.objects.create(
            application = self.application,
            enviorment = self.enviorment,
            active = True
        )

    def test_create_a_setting(self):

        setting = Setting.objects.create(
            configuration = self.configuration,
            key = "test",
            value = "this is a test"
        )

        self.assertGreater(setting.id, 0)

                
    def test_get_setting_by_key(self):

        Setting.objects.create(
            configuration = self.configuration,
            key = "test",
            value = "this is a test"
        )

        setting = Setting.objects.get(key="test")
        self.assertEqual(setting.key, "test")
        self.assertEqual(setting.configuration, self.configuration)
        self.assertEqual(setting.value, "this is a test")
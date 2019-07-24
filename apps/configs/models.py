from django.db import models


class Enviorment(models.Model):

    name = models.CharField(max_length=255)

    def __str__:
        return self.name


class Application(models.Model):

    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)   
         

class Configuration(models.Model):

    application = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    enviorment = models.ForeignKey(to=Enviorment, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

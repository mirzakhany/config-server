from django.db import models
import uuid


class Environment(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Application(models.Model):

    name = models.CharField(max_length=255)
    app_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
         

class Configuration(models.Model):

    application = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    environment = models.ForeignKey(to=Environment, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s-%s" % (self.application, self.environment)

    class Meta:
        unique_together = ['application', 'environment']


class Setting(models.Model):

    configuration = models.ForeignKey(to=Configuration, on_delete=models.CASCADE)
    key = models.CharField(max_length=300, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

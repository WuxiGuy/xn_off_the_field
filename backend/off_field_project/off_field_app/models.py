from django.db import models

# Create your models here.

class OffFieldApp(models.Model):
    '''
    define the django model
    Each field is specified as a class attribute, 
    and each attribute maps to a database column.

    attribute samples:
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    Run the Python script: python manage.py makemigrations off_field_app
    after set up attributes.
    '''

    def _str_(self):
        return self.title
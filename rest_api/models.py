from django.db import models

# Create your models here.
class EmoloyeeInfo(models.Model):
	emp_id = models.IntegerField(primary_key=True)
	emp_firstname = models.CharField(max_length=255, unique=True)
	emp_lastname = models.CharField(max_length=255)
	emp_salary = models.FloatField()
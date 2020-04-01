from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField('Company name',max_length=100)
    description = models.TextField('Company description')
    city = models.CharField("City name",max_length=100)
    address = models.TextField("Company address")

    def __str__(self):
        return self.name

    def short(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'


class Vacancy(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField('Vacancy name',max_length=100)
    description = models.TextField('Vacancy description')
    salary = models.FloatField('Vacancy salary')

    def __str__(self):
        return self.name

    def short(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }

    class Meta:
        verbose_name='Vacancy'
        verbose_name_plural='Vacancies'
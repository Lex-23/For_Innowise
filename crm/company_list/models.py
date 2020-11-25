from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    foundation = models.DateField()
    partnership = models.ManyToManyField(
        'self',
        symmetrical=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def getPartner(self):
        return self.partnership.values_list('name')


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def company_name(self):
        return self.company.name

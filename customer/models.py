from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=500,  blank=False, null=False)
    addr = models.CharField(max_length=200,  blank=False, null=False)
    city = models.CharField(max_length=100,  blank=False, null=False)
    state = models.CharField(max_length=100,  blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15,  blank=False, null=False)
    email = models.EmailField(default='',null=True,blank=True)
    # export_to_csv = models.BooleanField(default=False)
 
    def __str__(self):
        return self.name


class Visits(models.Model):
    status = {
        ('Green Zone', 'GREEN ZONE'),
        ('OrangeZone','ORANGE ZONE'),
        ('Red Zone','RED ZONE'),
        ('Containment Zone','CONTAINMENT ZONE'),
    }
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=False,blank=False)
    zone_status = models.CharField(null=True,blank=True, choices=status, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    narration = models.CharField(max_length=1000)
    along_with = models.IntegerField(default=0)



    

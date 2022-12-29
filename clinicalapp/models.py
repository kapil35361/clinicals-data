from django.db import models

class patient(models.Model):
    GENDER=[('male', 'MALE'),('female', 'FEMALE')]
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    Age=models.IntegerField()
    Gender=models.CharField(choices=GENDER,max_length=10)

    def __str__(self): 
        return f'{self.firstName}'



class ClinicalData(models.Model):
    COMPONENT=[('hw', 'Height/Weight'),('bloodpresure', 'BloodPresure'),('heartrate','Heartrate')]
    componentName=models.CharField(choices=COMPONENT,max_length=15)
    componentValue=models.CharField(max_length=20)
    measureDate=models.DateField(auto_now_add=True)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)
    

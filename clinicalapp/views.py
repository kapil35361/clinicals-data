from django.shortcuts import render,redirect
from clinicalapp.models import patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from  clinicalapp.forms import ClinicalDataForms





class PatientListView(ListView):
      model=patient



class PatientCreateView(CreateView):
      model=patient
      fields='__all__'
      success_url=reverse_lazy('index')


class PatientUpdateView(UpdateView):
      model=patient
      fields='__all__'
      success_url=reverse_lazy('index')

class PatientDeleteView(DeleteView):
      model=patient 
      success_url=reverse_lazy('index') 



def AddClinicalData(request,**kwargs):
      
      form= ClinicalDataForms()
      patients=patient.objects.get(id=kwargs['pk']) 
      if request.method=='POST':
            form=ClinicalDataForms(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/')
      return render(request, 'clinicalapp/addclinicaldata.html',{'form':form,'patient':patients})    

def Analyze(request,**kwargs):
      data=ClinicalData.objects.filter(patient_id=(kwargs['pk']))
      responsedata=[]
      for eachEntry in data:
            if eachEntry.componentName=='hw':
                  heightandweight=eachEntry.componentValue.split('/')
                  if len(heightandweight)>1:
                   feettometer=float(heightandweight[0])*4536
                   BMI=float((heightandweight[1]))/(feettometer*feettometer)
                   bmiEntry=ClinicalData()
                   bmiEntry.componentName='BMI'
                   bmiEntry.componentValue=BMI
                   responsedata.append(bmiEntry)
            responsedata.append(eachEntry)       




                  
               
      return render(request, 'clinicalapp/generatereport.html',{'data':responsedata})         

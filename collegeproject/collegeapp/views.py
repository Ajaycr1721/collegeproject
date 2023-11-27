from django.shortcuts import redirect, render
from collegeapp.models import reg
# Create your views here.
# def display(request):
#     return render(request,'college1.html')
def doc1(request):
    if request.method=='POST':
        obj=reg()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.phonenumber=request.POST.get("phone")
        obj.age=request.POST.get("age")
        obj.save()
        return redirect('status')
    return render(request,'college1.html')
def status(request):
    obj=reg.objects.all()
    return render(request,'table.html',{'data':obj})
def update(request,p):
    obj=reg.objects.get(id=p)
    if request.method=='POST':
        obj=reg.objects.get(id=p)
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.phonenumber=request.POST.get("phone")
        obj.age=request.POST.get("age")
        obj.save()
        return redirect('status')
    return render(request,'update.html',{'data':obj})
def deleteform(request,p):
    obj=reg.objects.get(id=p)
    obj.delete()
    return status(request)


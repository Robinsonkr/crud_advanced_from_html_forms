from django.shortcuts import render,redirect
from .models import Employee,Department
 
def home(request):
    all_employees = Employee.objects.select_related("department").all()
 
    context ={
        'all_employees':all_employees,
    
         
        }
    return render(request,'crud_app/show.html',context)
 
def add_employee(request):
    department = Department.objects.all()
    all_employees = Employee.objects.select_related("department").all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        mode = request.POST.get('mode')
        description = request.POST.get('description')
        image = request.FILES['image']
        department =Department.objects.get(id=request.POST.get('department'))
        status = request.POST.get('status')

 
        employee = Employee(name=name,email=email,phone=phone,website=website,mode=mode,department=department,status=status,image=image)
        employee.save()
        return redirect('home')

    context ={

        'department':department,
        'all_employees':all_employees,
         
        }
    return render(request,'crud_app/add.html',context)

def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')

def edit_employee(request,id):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        mode = request.POST.get('mode')
        status = request.POST.get('status')
        description = request.POST.get('description')
        image = request.FILES['image']
        employee = Employee.objects.get(id=id)

        employee.name = name
        employee.email = email
        employee.phone = phone
        employee.description = description
        
        
        employee.website = website
        employee.mode = mode
        employee.image = image

        employee.save() 
        return redirect('home')
 
    else:
        employee = Employee.objects.get(id=id)

        context = {
            'employee':employee,

        }
        return render(request,'crud_app/edit.html',context)

def search_employee(request):
    if request.method == "POST":
        searched = request.POST['searched']
        employee =  Employee.objects.filter(name__contains=searched)
        return render(request, 'crud_app/search.html', {'searched':searched,'employee':employee})
    else:
        return render(request, 'crud_app/search.html', {})
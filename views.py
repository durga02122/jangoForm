from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .models import Student
from .forms import AddStudentForm


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
    
def signin(request): 
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST.get('pass1')
       
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

class about(View):
    def get(self,request):
        stu_data =Student.objects.all()
        return render(request, 'core/about.html',{'studata' :stu_data}) 

class Add_Student(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form':fm})
    def post(self,request):
        fm =AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/about')
        else:
            return render(request, 'core/add-student.html',{'from':fm})
     
class Delete_Student(View):
    def post(self,request):
        data =request.POST 
        id = data.get('id') 
        Studata =Student.objects.get(id=id)
        Studata.delete()
        return redirect('/about')

class EditStudent(View):
    def get(self,request, id):
        stu =Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request,'core/edit-student.html', {'form':fm})

    def post(self,request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/about')






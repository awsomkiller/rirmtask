from django.shortcuts import redirect, render
from .form import student_data, studentacademics_data
from .models import students, studentacademics

# Create your views here.
def home(request):
    return render(request, 'index.html')

def addStudent(request):
    form = student_data(request.POST or None)
    if form.is_valid():
        rollnumber = form.cleaned_data.get("roll_number")
        name = form.cleaned_data.get("name")
        studentclass = form.cleaned_data.get("student_class")
        school = form.cleaned_data.get("school_name")
        mobile = form.cleaned_data.get("mobile")
        address = form.cleaned_data.get("address")
        student = students(roll_number=rollnumber, name=name, student_class=studentclass, school_name=school, mobile=mobile, address = address)
        student.save()
        return redirect('/')
    else:
        return render(request, 'studentregisteration.html', {'form':form, 'data':"Student Data"})
def addAcademic(request):
    form = studentacademics_data(request.POST or None)
    if form.is_valid():
        id = form.cleaned_data.get("id")
        roll = form.cleaned_data.get("roll_number")
        roll_number =  students.objects.get(roll_number=roll)
        maths = form.cleaned_data.get("maths")
        physics = form.cleaned_data.get("physics")
        chemistry = form.cleaned_data.get("chemistry")
        biology = form.cleaned_data.get("biology")
        english = form.cleaned_data.get("english")
        obj = studentacademics(id=id, roll_number=roll_number, maths=maths, physics=physics, chemistry=chemistry, biology=biology, english=english)
        obj.save()
        return redirect('/')
    else:
        return render(request, 'studentregisteration.html', {'form':form, 'data':"Student Academics Data"})

def viewData(request):
    student = students.objects.all()
    data_list = []
    if student is not None:
        index = 1
        for s in student:
            temp = {}
            temp['index']=index
            temp['name']=s.name
            obj = None
            try:
                obj = studentacademics.objects.get(roll_number=s)
            except:
                pass
            temp['math']=obj.maths
            temp['english']=obj.english
            temp['physics']=obj.physics
            temp['chemistry']=obj.chemistry
            temp['biology']=obj.biology
            data_list.append(temp)
            index = index+1
        return render(request, 'view.html', {'data':True, 'datalist':data_list})
    else:
        return render(request, 'view.html',{'data':False})
            


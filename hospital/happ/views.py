from django.shortcuts import render,redirect,get_object_or_404
from happ.models import Department,User,Patient,Doctor
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'index.html')

def adminhome(request):
    return render(request,'adminhome.html')

def doctorhome(request):
    return render(request,'doctorhome.html')

def patienthome(request):
    pat_id = request.session.get('pat_id')  # Get patient ID from session
    return render(request, 'patienthome.html', {'pat_id': pat_id})


def page(request):
    return render(request,'page.html')



def dep_add(request):
    if request.method=='POST':
        d=request.POST['dep']
        x=Department.objects.create(dep_name=d)
        x.save()
        return HttpResponse("success")
    else:
        return render(request,'dep_add.html')

def reg_patient(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        g=request.POST['gender']
        ph=request.POST['phone']
        print(d,f,l,e,u,p,ad,g,ph)
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='Patient',is_active=True)
        x.save()
        y=Patient.objects.create(pid=x,depid_id=d,Age=a,Address=ad,gender=g,phone=ph)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'reg_patient.html',{'x1':x})

def reg_doctor(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='doctor')
        x.save()
        y=Doctor.objects.create(dcid=x,depid_id=d,Qualification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'reg_doctor.html',{'x1':x})
    
def viewpatients(request):
    x=Patient.objects.all()
    return render(request,'viewpatients.html',{'x1':x})

def viewdoctors(request):
    x=Doctor.objects.all()
    return render(request,'viewdoctors.html',{'x1':x})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages

def logins(request):
    if request.method == "POST":
        u = request.POST.get('username', '').strip()
        p = request.POST.get('password', '').strip()
        user = authenticate(request, username=u, password=p)

        if user:
            login(request, user)

            if user.is_superuser:
                return redirect('adminhome')

            elif hasattr(user, 'usertype'):
                usertype = user.usertype.lower()

                if usertype == "doctor":
                    request.session['doc_id'] = user.id
                    return redirect('doctorhome')

                elif usertype == "patient":
                    request.session['pat_id'] = user.id  # ✅ Store patient ID in session
                    return redirect('patienthome')

            messages.error(request, "Invalid user type. Please contact support.")  
        else:
            messages.error(request, "Invalid username or password.")  

    return render(request, 'logins.html')

    
def lgout(request):
    logout(request)
    return redirect(logins)

def log(request):
    return render(request,'log.html')

def updatepat(request):
    pat_id = request.session.get('stu_id')  # Get patient ID from session

    if not pat_id:
        return HttpResponse("Error: No patient ID found in session.")

    try:
        patient = Patient.objects.get(pat_id=pat_id)
        user = User.objects.get(id=pat_id)
    except Patient.DoesNotExist:
        return HttpResponse("Error: Patient not found.")
    except User.DoesNotExist:
        return HttpResponse("Error: User not found.")

    return render(request, 'updatepatient.html', {'view': patient, 'data': user})

def updatepatient(request, uid):
    try:
        pat = Patient.objects.get(id=uid)
        user = User.objects.get(id=pat.pid.id)  # Get User using pid relationship
    except Patient.DoesNotExist:
        return HttpResponse("Error: Patient not found.")
    except User.DoesNotExist:
        return HttpResponse("Error: User not found.")

    if request.method == "POST":
        # Update User details
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.username = request.POST['uname']
        user.save()

        # Update Patient details
        pat.age = request.POST['age']
        pat.address = request.POST['address']
        pat.phone = request.POST['phone']
        pat.gender = request.POST['gender']
        pat.save()

        return redirect('patienthome')  # Redirect to patient home

    # If request is GET, render the update form
    return render(request, 'updatepatient.html', {'view': pat, 'data': user})

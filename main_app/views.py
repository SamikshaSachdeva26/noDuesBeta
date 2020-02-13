from django.shortcuts import render
from main_app.forms import StudentUserForm,StudentsInfoForm, LabUserForm, LabInfoForm, BTPUserForm, BTPInfoForm, OtherUserForm, HODUserForm, HODInfoForm, OtherInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from main_app.models import Department, StudentUserInfo, HODUserInfo, LabUserInfo, BTPUserInfo, OtherUserInfo, LabRequests, BTPRequest, OtherRequest
import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# Create your views here.

#for logout
@login_required
def user_logout(request):
    logout(request);
    return HttpResponseRedirect(reverse('mainPage'))


#to figure out whether user is logged in or not: if not, login page is displayed, otherwise index page
def mainPage(request):

    if request.user.is_authenticated:

        #if logged in
        #to check the type of user currently logged in. If user is a student, he must have a profile in 'StudentUserInfo' database

        dict1 = StudentUserInfo.objects.filter(user=request.user)
        if len(dict1)>0:
            return HttpResponseRedirect(reverse('studentIndex'))
        else:
            dict2 = LabUserInfo.objects.filter(user=request.user)
            if len(dict2)>0:
                return HttpResponseRedirect(reverse('labIndex'));
            else:
                dict3 = OtherUserInfo.objects.filter(user=request.user)
                if len(dict3)>0:
                    return HttpResponseRedirect(reverse('otherIndex'))
                else:
                    print("lalalala")
                    dict4 = BTPUserInfo.objects.filter(user=request.user)
                    if len(dict4)>0:
                        return HttpResponseRedirect(reverse('btpIndex'))
                    else:
                        dict5 = HODUserInfo.objects.filter(user=request.user)
                        if len(dict5)>0:
                            return HttpResponseRedirect(reverse('hodIndex'))
                        else:
                            return HttpResponse("unable to log in")

    else:
        #not logged in
        return render(request, 'main_app/base.html')

def studentIndex(request):

    if request.POST:
        print(request.POST)
        student = StudentUserInfo.objects.get(user=request.user)
        






        varlib = request.POST.get('Library/CCC',None)
        if varlib:
            # print("Print-----varlib")
            try:
                print("try....")
                vlib = OtherRequest.objects.get(student=student, other=OtherUserInfo.objects.get(user__username="LibraryCCC"))
                print("Print-----varlib",vlib)
            except:
                print("vlib none")
                vlib = None

            if vlib:
                vlib.delete()
                print("vlib deleted")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username="LibraryCCC"),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
                print("vlib created")
            else:
                print("else bahar wala")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username="LibraryCCC"),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )


        varlib = request.POST.get('Gymkhana',None)
        if varlib:
            # print("Print-----varlib")
            try:
                print("try....")
                vlib = OtherRequest.objects.get(student=student, other=OtherUserInfo.objects.get(user__username="Gymkhana"))
                print("Print-----varlib",vlib)
            except:
                print("vlib none")
                vlib = None

            if vlib:
                vlib.delete()
                print("vlib deleted")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username="Gymkhana"),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
                print("vlib created")
            else:
                print("else bahar wala")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username="Gymkhana"),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
           # lib.save()
        varlib = request.POST.get('HOSTEL',None)
        if varlib:
            # print("Print-----varlib")
            try:
                print("try....")
                vlib = OtherRequest.objects.get(student=student, other=OtherUserInfo.objects.get(user__username=varlib))
                print("Print-----varlib",vlib)
            except:
                print("vlib none")
                vlib = None

            if vlib:
                vlib.delete()
                print("vlib deleted")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username=varlib),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
                print("vlib created")
            else:
                print("else bahar wala")
                lib = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username=varlib),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )







        # varhostel = request.POST.get('HOSTEL',None)
        # if varhostel:
        #     hos = OtherRequest.objects.create(  other=OtherUserInfo.objects.get(user__username=varhostel),
        #                                         student=StudentUserInfo.objects.get(user=request.user),
        #                                         remark="",
        #                                         date_sent=datetime.date.today(),
        #                                         approval_status=0
        #                                         )
          #  hos.save()


        varbtp = request.POST.get('BTP',None)
        if varbtp:
            try:
                btpt = BTPRequest.objects.get(student=student)
            except:
                btpt = None

            if btpt:
                btpt.delete()
                btp = BTPRequest.objects.create(  btp=BTPUserInfo.objects.get(user__username=varbtp),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
           
            else:
                 btp = BTPRequest.objects.create(  btp=BTPUserInfo.objects.get(user__username=varbtp),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
           

          #  btp.save()


        
        labs = LabUserInfo.objects.filter(department_id=student.department_id)
        #print(labs)
        for lab in labs :
            #print(lab)
            # print(lab.id," ",lab.user.username)
            varlab = request.POST.get(lab.user.username, None)
            # print(varlab)
            if varlab:
                try:
                    ll = LabRequests.objects.get(student=student, lab=LabUserInfo.objects.get(user__username=varlab))
                except:
                    ll = None
                if ll:
                    ll.delete()
                    labx = LabRequests.objects.create(  lab=LabUserInfo.objects.get(id=lab.id),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
                else:
                    labx = LabRequests.objects.create(  lab=LabUserInfo.objects.get(id=lab.id),
                                                student=StudentUserInfo.objects.get(user=request.user),
                                                remark="",
                                                date_sent=datetime.date.today(),
                                                approval_status=0
                                                )
              #  labx.save()


        return HttpResponseRedirect(reverse('mainPage'))




    if request.user.is_authenticated:

        #render student's requests from database

        labRequests = LabRequests.objects.filter(student__user=request.user)
        btpRequests = BTPRequest.objects.filter(student__user=request.user)
        otherRequests = OtherRequest.objects.filter(student__user=request.user)
        return render(request, 'main_app/student_main_page.html', {'labRequests': labRequests, 'btpRequests': btpRequests, 'otherRequests': otherRequests});

    return HttpResponseRedirect(reverse('mainPage'))



def labIndex(request):

    p = 0
    if request.POST:
        print(request.POST);
        if 'Accept' in request.POST:
            for req in LabRequests.objects.filter(lab__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 1
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                # except:
                # print("Nahi hua")

        elif 'Reject' in request.POST:
            for req in LabRequests.objects.filter(lab__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 3
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                # except:
                # print("Nahi hua")
        requests = LabRequests.objects.filter(lab__user=request.user, approval_status=0)
        return render(request, 'main_app/lab_main_page.html', {'requests': requests, 'p' : p});


    if request.user.is_authenticated:

        #render requests to a particular lab

        requests = LabRequests.objects.filter(lab__user=request.user, approval_status=0)
        if requests:
            p = 1
        return render(request, 'main_app/lab_main_page.html', {'requests': requests, 'p' : p});

    return HttpResponseRedirect(reverse('mainPage'))

def btpIndex(request):

    p = 0
   

    if request.POST:
        print(request.POST);
        if 'Accept' in request.POST:
            for req in BTPRequest.objects.filter(btp__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 1
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                # except:
                # print("Nahi hua")

        elif 'Reject' in request.POST:
            for req in BTPRequest.objects.filter(btp__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 3
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                # except:
                # print("Nahi hua")
        requests = BTPRequest.objects.filter(btp__user=request.user, approval_status=0)
        return render(request, 'main_app/btp_main_page.html', {'requests': requests, 'p' : p});


    if request.user.is_authenticated:

        #load requests to a particular btp prof

        requests = BTPRequest.objects.filter(btp__user=request.user, approval_status=0)
        if requests:
            p = 1
        return render(request, 'main_app/btp_main_page.html', {'requests': requests, 'p' : p});

    return HttpResponseRedirect(reverse('mainPage'))

def otherIndex(request):

    p = 0

    if request.POST:
        print(request.POST);
        if 'Accept' in request.POST:
            for req in OtherRequest.objects.filter(other__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 2
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                # except:
                # print("Nahi hua")

        elif 'Reject' in request.POST:
            for req in OtherRequest.objects.filter(other__user=request.user, approval_status=0):
                # try:
                p = 1
                stud = str(req.student.rollnumber)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 3
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()

        requests = OtherRequest.objects.filter(other__user=request.user, approval_status=0)
        return render(request, 'main_app/other_main_page.html', {'requests': requests, 'p' : p });


    if request.user.is_authenticated:

        #load requests to library etc.

        requests = OtherRequest.objects.filter(other__user=request.user, approval_status=0)
        if requests:
            p = 1
        return render(request, 'main_app/other_main_page.html', {'requests': requests, 'p' : p });

    return HttpResponseRedirect(reverse('mainPage'))


def hodIndex(request):

   
    if request.POST:
        print(request.POST)

        dicts = HODUserInfo.objects.get(user=request.user)

        if 'AcceptLAB' in request.POST:
            for req in LabRequests.objects.filter(lab__department=dicts.department, approval_status=1):
                # try:
              
                stud = str(req.student.rollnumber)+str(req.lab.user.username)
                print(stud)
                print(request.POST.getlist(stud))
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    print("YESSS")
                    req.approval_status = 2
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                else:
                    print("Nahi hua")

        elif 'RejectLAB' in request.POST:
            for req in LabRequests.objects.filter(lab__department=dicts.department, approval_status=1):
                # try:
               
                stud = str(req.student.rollnumber)+str(req.lab.user.username)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 3
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                else:
                    print("Nahi hua")

        if 'AcceptBTP' in request.POST:
            for req in BTPRequest.objects.filter(btp__department=dicts.department, approval_status=1):
                # try:
              
                stud = str(req.student.rollnumber)+str(req.btp.user.username)
                print(stud)
                print(request.POST.getlist(stud))
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    print("YESSS")
                    req.approval_status = 2
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                else:
                    print("Nahi hua")



        elif 'RejectBTP' in request.POST:
            for req in BTPRequest.objects.filter(btp__department=dicts.department, approval_status=1):
                # try:
              
                stud = str(req.student.rollnumber)+str(req.btp.user.username)
                print(stud)
                print(request.POST.getlist(stud)[0])
                if request.POST.getlist(stud)[0] == 'YES':
                    # req.update(approval_status=1, remark=request.POST.getlist(stud))
                    req.approval_status = 3
                    req.remark = request.POST.getlist(stud)[1]
                    req.save()
                else:
                    print("Nahi hua")

     #   return HttpResponseRedirect(reverse('mainPage'))













   # print(p,q);





    if request.user.is_authenticated:

        #load requests to library etc.

        dicts = HODUserInfo.objects.filter(user=request.user)
        for dict in dicts:
            department = dict.department
            requests = LabRequests.objects.filter(lab__department=department, approval_status=1)
            requests2=BTPRequest.objects.filter(btp__department=department, approval_status=1)
            return render(request, 'main_app/hod_main_page.html', {'requests': requests, 'requests2':requests2 });



    return HttpResponseRedirect(reverse('mainPage'))



def studentBTP(request):

    if request.user.is_authenticated:

        #load student's btp requests on one page separately

        btpRequests = BTPRequest.objects.filter(student__user=request.user)
        return render(request, 'main_app/student_btp_page.html', {'btpRequests': btpRequests})

    return render(request, 'main_app/student_btp_page.html')

def studentLab(request):
    if request.user.is_authenticated:

        #load student's lab requests separately

        labRequests = LabRequests.objects.filter(student__user=request.user)
        return render(request, 'main_app/student_lab_page.html', {'labRequests': labRequests})

    return render(request, 'main_app/student_lab_page.html')

def studentOther(request):
    if request.user.is_authenticated:

        #load student's other requests separately

        otherRequests = OtherRequest.objects.filter(student__user=request.user)
        return render(request, 'main_app/student_other_page.html', {'otherRequests': otherRequests})

    return render(request, 'main_app/student_other_page.html')

def registerStudent(request):
    registered = False

    #self explanatory

    if request.method == "POST":
        user_form = StudentUserForm(data=request.POST)
        info_form = StudentsInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()

            profile = info_form.save(commit=False)
            profile.user = user;

            profile.save()

            registered = True

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('studentIndex'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print("someone tried to login and failed")
                print("Username: {} Password: {}".formar(username, password))
                return HttpResponse("invalid login details supplied")


        else:
            print(user_form.errors, info_form.errors)

    else:

        user_form=StudentUserForm()
        info_form=StudentsInfoForm()

    return render(request, 'main_app/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 0})


def registerLab(request):
    registered = False

    #self explanatory

    if request.method == "POST":
        user_form = LabUserForm(data=request.POST)
        info_form = LabInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()

            profile = info_form.save(commit=False)
            profile.user = user;

            profile.save()

            registered = True

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('labIndex'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print("someone tried to login and failed")
                print("Username: {} Password: {}".formar(username, password))
                return HttpResponse("invalid login details supplied")

        else:
            print(user_form.errors, info_form.errors)

    else:

        user_form=LabUserForm()
        info_form=LabInfoForm()

    return render(request, 'main_app/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 1})

def registerHOD(request):
    registered = False

    #self explanatory

    if request.method == "POST":
        user_form = HODUserForm(data=request.POST)
        info_form = HODInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()

            profile = info_form.save(commit=False)
            profile.user = user;

            profile.save()

            registered = True

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('hodIndex'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print("someone tried to login and failed")
                print("Username: {} Password: {}".formar(username, password))
                return HttpResponse("invalid login details supplied")

        else:
            print(user_form.errors, info_form.errors)

    else:

        user_form=HODUserForm()
        info_form=HODInfoForm()

    return render(request, 'main_app/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 4})



def registerOther(request):
    registered = False

    #self explanatory

    if request.method == "POST":
        user_form = OtherUserForm(data=request.POST)
        info_form = OtherInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()

            profile = info_form.save(commit=False)
            profile.user = user;

            profile.save()

            registered = True

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('otherIndex'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print("someone tried to login and failed")
                print("Username: {} Password: {}".formar(username, password))
                return HttpResponse("invalid login details supplied")

        else:
            print(user_form.errors, info_form.errors)

    else:

        user_form=OtherUserForm()
        info_form=OtherInfoForm()

    return render(request, 'main_app/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 2})

def registerBTP(request):
    registered = False

    #self explanatory

    if request.method == "POST":
        user_form = BTPUserForm(data=request.POST)
        info_form = BTPInfoForm(data=request.POST)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()

            profile = info_form.save(commit=False)
            profile.user = user;

            profile.save()

            registered = True

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('btpIndex'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print("someone tried to login and failed")
                print("Username: {} Password: {}".formar(username, password))
                return HttpResponse("invalid login details supplied")

        else:
            print(user_form.errors, info_form.errors)

    else:

        user_form=BTPUserForm()
        info_form=BTPInfoForm()

    return render(request, 'main_app/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 3})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                #to check the type of user to log in

                dict1 = StudentUserInfo.objects.filter(user=request.user)
                if len(dict1)>0:
                    return HttpResponseRedirect(reverse('studentIndex'))
                else:
                    dict2 = LabUserInfo.objects.filter(user=request.user)
                    if len(dict2)>0:
                        return HttpResponseRedirect(reverse('labIndex'));
                    else:
                        dict3 = OtherUserInfo.objects.filter(user=request.user)
                        if len(dict3)>0:
                            return HttpResponseRedirect(reverse('otherIndex'))
                        else:
                            dict4 = BTPUserInfo.objects.filter(user=request.user)
                            if len(dict4)>0:
                                return HttpResponseRedirect(reverse('btpIndex'))
                            else:
                                dict5 = HODUserInfo.objects.filter(user=request.user)
                                if len(dict5)>0:
                                    return HttpResponseRedirect(reverse('hodIndex'))
                                else:
                                    return HttpResponse("unable to log in")

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("someone tried to login and failed")
            print("Username: {} Password: {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'main_app/base.html', {})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('studentIndex'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main_app/change_password.html', {
        'form': form
    })

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('studentIndex'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main_app/change_password.html', {
        'form': form
    })

def apply_page(request):
    student = StudentUserInfo.objects.get(user=request.user)
    # print(student)
    #dir(student)
    # print(type(student))
    # variables = [i for i in dir(student) if not callable(i)]

    # btpreq = BTPRequest.objects.get(student=student)
    # print(btpreq)
    # print([f.get_attname() for f in student._meta.fields])
    # print("----------------------------------------------\n--------------------------------\n")

    try:
        othreqs = OtherRequest.objects.filter(student=student)
    except OtherRequest.DoesNotExist:
        othreqs = None


    try:
        labreqs = LabRequests.objects.filter(student=student)
    except LabRequests.DoesNotExist:
        labreqs = None


    try:
        btpreq = BTPRequest.objects.get(student=student)
    except BTPRequest.DoesNotExist:
        btpreq = None

    try:
        btps = BTPUserInfo.objects.all()
    except BTPUserInfo.DoesNotExist:
        btps = None

    try:
        labs = LabUserInfo.objects.filter(department_id=student.department_id)
    except LabUserInfo.DoesNotExist:
        labs = None




    l = 0
    h = 0
    b = 0
    op = 0
    k = 0
    g = 0
    arr = []
    # print(labs)

    if labs:

        for labx in labs:

            if labreqs:

                try:
                    labrc = labreqs.get(lab=labx)
                except:
                    labrc = None
                print(labrc,"labrc")
                if labrc:
                    print(labrc,"labrc",labrc.approval_status)
                    if labrc.approval_status in (0,1,2):
                        arr.append(1)
                    else:
                        arr.append(0)
                        op = 1
                else:
                    arr.append(0)
                    op = 1
            else:

                arr.append(0)
                op = 1



    # print(arr)






    if btpreq:
        if btpreq.approval_status in (0,1,2):
            b = 1


    for req in othreqs:
        if req.other.user.username == 'LibraryCCC' and req.approval_status in (0,1,2) :
            l = 1
        if req.other.user.username == 'Gymkhana' and req.approval_status in (0,1,2) :
            g = 1
        if req.other.user.username == 'LOHIT'  and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'SIANG' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'DIHING' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'MANAS' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'KAPILI' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'UMIAM' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'BRAHMAPUTRA' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'BARAK' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'KAMENG' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'MSH' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'DHANSIRI' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'SUBANSIRI' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'DIBANG' and req.approval_status in (0,1,2) :
            h = 1
        if req.other.user.username == 'DISANG' and req.approval_status in (0,1,2) :
            h = 1



    if l == 1 and h == 1 and b == 1 and op == 0 and g == 1 :
        k = 1



    print(l,h,b,op,k)
    return render(request, 'main_app/apply.html', {'student' : student, 'btps' : btps, 'labs' : labs, 'labreqs': labreqs, 'othreqs': othreqs, 'btpreq' : btpreq,
                                                     'l' : l, 'h' : h, 'b' : b ,'op' : op , 'k' : k , 'arr' : arr, 'g' : g })

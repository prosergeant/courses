from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import DetailView
from django.views.generic.base import View
from django.template.defaulttags import register

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

#from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@register.filter
def get_range(value):
    return range(value)


@register.filter
def get_range1(value):
    return range(value+1)


@register.filter
def to_int(value):
    return int(value)


# lesson_data = lessons.objects.all()


def index(request):
    return render(request, 'main/index.html')


def ab(request):
    if request.method == 'POST':
        request.session['has_commented'] = True

    return render(request, 'main/about.html', {"comm_ses": request.session.get('has_commented')})
    #if request.session.get('has_commented', False):
    #    return HttpResponse("Вы уже отправили комментарий")
    #request.session['has_commented'] = True
    #return HttpResponse('Спасибо за ваш комментарий!')


def course(request):
    all_courses = Course.objects.all()
    return render(request, 'main/course.html', {'lesson_data': all_courses})


def cabinet(request):
    return render(request, 'main/cabinet.html')


def classes(request):
    if not request.user.is_anonymous:
        if request.user.first_time == True:
            request.user.first_time = False
            #request.user.save()

            """
            добавляет в личный кабинет новому юзеру первые 3 урока для всех классов и предметов для направления НИШ
            for i in range(11):
                some_var_for_courseRUS = Course.objects.filter(klass=i+1, direction='nis', subject='rus')
                some_var_for_courseKAZ = Course.objects.filter(klass=i+1, direction='nis', subject='kaz')
                some_var_for_courseENG = Course.objects.filter(klass=i+1, direction='nis', subject='eng')
                some_var_for_courseMAT = Course.objects.filter(klass=i+1, direction='nis', subject='mat')
                
                for j in range(3):
                    new_purchaseRUS = Purchased(user=request.user, course=some_var_for_courseRUS[i])
                    new_purchaseRUS.save()
                    new_purchaseKAZ = Purchased(user=request.user, course=some_var_for_courseKAZ[i])
                    new_purchaseKAZ.save()
                    new_purchaseENG = Purchased(user=request.user, course=some_var_for_courseENG[i])
                    new_purchaseENG.save()
                    new_purchaseMAT = Purchased(user=request.user, course=some_var_for_courseMAT[i])
                    new_purchaseMAT.save()
            """

            """
            Временное решение для покупки автоматом первых уроков
            
            courses1stNIS = Course.objects.filter(klass=1, direction='nis')
            courses1stKTL = Course.objects.filter(klass=1, direction='ktl')
            courses2ndNIS = Course.objects.filter(klass=2, direction='nis')
            courses2ndRFM = Course.objects.filter(klass=2, direction='rfm')
            courses6thNIS = Course.objects.filter(klass=6, direction='nis')

            for i in range(2):
                new_purchase = Purchased(user=request.user, course=courses1stNIS[i])
                new_purchase.save()

            for i in range(1):
                new_purchase = Purchased(user=request.user, course=courses1stKTL[i])
                new_purchase.save()

            for i in range(2):
                new_purchase = Purchased(user=request.user, course=courses2ndNIS[i])
                new_purchase.save()

            for i in range(2):
                new_purchase = Purchased(user=request.user, course=courses2ndRFM[i])
                new_purchase.save()

            for i in range(1):
                new_purchase = Purchased(user=request.user, course=courses6thNIS[i])
                new_purchase.save()
            """

    return render(request, 'main/classes.html')


class CourseDetailView(View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        return render(request, "main/lesson_detail.html", {
            "lesson": course
        })



class ClassesDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, klass_id, dir_id, sub_id, classes_id):
        
        class_data = Course.objects.filter(id=int(classes_id))
        quest_data_temp = Quest.objects.all()
        quest_data = []
        cls = class_data[0]
        can_read = False
        answers_temp = []
        if request.user.is_authenticated:
            answers_temp = Answer.objects.filter(user=request.user)
        answers = []

        curr_purchase_lesson = None
        if request.user.is_authenticated:
            try:
                curr_purchase_lesson = Purchased.objects.get(user=request.user, course=cls)
            except Exception:
                curr_purchase_lesson = None
                #print('user: ' + request.user.email + ' not have this lesson')

        curr_prem = False
        curr_prem_time = None

        if curr_purchase_lesson is not None:
            if self.assertFalse( curr_purchase_lesson.has_prem() ):
                curr_prem = True
                curr_prem_time = curr_purchase_lesson.until

        """
        purchase_data = Purchased.objects.all()
        for i in purchase_data:
            if request.user == i.user:
                if i.course == cls:
                    can_read = True
        """

        purchase_data = Purchased.objects.filter(user=request.user)
        for i in purchase_data:
            if i.course == cls:
                can_read = True

        for i in quest_data_temp:
            if i.course == cls:
                quest_data.append(i)

        for i in answers_temp:
            for j in quest_data:
                if i.quest == j:
                    answers.append(i)

        """
        return render(request, "main/dashboard_classes_detail.html", {"lesson": cls,
                                                            "can_read": can_read,
                                                            "klass_id": klass_id,
                                                            "dir_id": dir_id,
                                                            "sub_id": sub_id,
                                                            "classes_id": classes_id,
                                                            "quest_data": quest_data,
                                                            "answers": answers,
                                                            "session_test_start": request.session.get('test_start'),
                                                            "user_is_premium": request.user.is_premium if request.user.is_authenticated else False,
                                                            "curr_prem": curr_prem,
                                                            "curr_prem_time": curr_prem_time})
        """
        
        json_course = Course.objects.get(id=int(classes_id))
        json_klass_id = json_course.klass
        json_dir_id = json_course.direction
        json_sub_id = json_course.subject

        
        data = { "user_email": request.user.email if request.user.is_authenticated else "anonymous",
                                                            "can_read": can_read,
                                                            "klass_id": json_klass_id,
                                                            "dir_id": json_dir_id,
                                                            "sub_id": json_sub_id,
                                                            "classes_id": int(classes_id),
                                                            #"quest_data": quest_data,
                                                            #"answers": answers,
                                                            "session_test_start": request.session.get('test_start'),
                                                            "user_is_premium": request.user.is_premium if request.user.is_authenticated else False,
                                                            "curr_prem": curr_prem,
                                                            "curr_prem_time": curr_prem_time}


        return Response(data, status=status.HTTP_201_CREATED) #JsonResponse(data)

    """

    def post(self, request, klass_id, dir_id, sub_id, classes_id, format = None):
        class_data = Course.objects.filter(id=int(classes_id))
        quest_data_temp = Quest.objects.all()
        quest_data = []
        cls = class_data[0]  
        can_read = False
        purchase_data = Purchased.objects.all()
        answers_temp = Answer.objects.all()
        answers = []

        for i in purchase_data:
            if request.user == i.user:
                if i.course == cls:
                    can_read = True

        for i in quest_data_temp:
            if i.course == cls:
                quest_data.append(i)

        for i in answers_temp:
            for j in quest_data:
                if i.quest == j:
                    answers.append(i)

        context = request.POST
        choice = context.get('answer')
        answered_modal = context.get('Modal')
        i_ans_modal = int(answered_modal)

        if quest_data[i_ans_modal-1].correct == choice:
            ans = Answer(user=request.user, quest=quest_data[i_ans_modal-1], right=True, start=True)
            ans.save()
        else:
            ans = Answer(user=request.user, quest=quest_data[i_ans_modal-1], right=False, start=True)
            ans.save()

        request.session['test_start'] = True

        return redirect('classes_detail', klass_id, dir_id, sub_id, classes_id)


        
        return render(request, "main/classes_detail_after.html", {"context": context, "choice": choice,
                                                            "lesson": cls,
                                                            "can_read": can_read,
                                                            "klass_id": klass_id,
                                                            "dir_id": dir_id,
                                                            "sub_id": sub_id,
                                                            "quest_data": quest_data,
                                                            "answers": answers
                                                            })
        """
    
    def assertFalse(self, some):
        if some == True:
            return True
        else:
            return False

    def post(self, request, klass_id, dir_id, sub_id, classes_id):
        context = request.POST

        #test handler
        cls = Course.objects.get(id=int(classes_id))
        quest_data_temp = Quest.objects.all()
        quest_data = []

        for i in quest_data_temp:
            if i.course == cls:
                quest_data.append(i)

        choice = context.get('answer')
        answered_modal = context.get('Modal')
        if answered_modal is None:
            answered_modal = -1
        i_ans_modal = int(answered_modal)

        if answered_modal == -1:
            print('do nothing')
        else:
            if quest_data[i_ans_modal-1].correct == choice:
                ans = Answer(user=request.user, quest=quest_data[i_ans_modal-1], right=True, start=True)
                ans.save()
                request.user.exp += 5
                request.user.save()
            else:
                ans = Answer(user=request.user, quest=quest_data[i_ans_modal-1], right=False, start=True)
                ans.save()

        request.session['test_start'] = True

        #premium handler
        prem = context.get('buy_prem')
        _7days = context.get('_7days')
        _30days = context.get('_30days')
        _90days = context.get('_90days')

        if _7days == 'yes':
            curr_purch = Purchased.objects.get(user=request.user, course=Course.objects.get(id=int(classes_id)))
            curr_purch.add_prem_7days()
            curr_purch.save()
        elif _30days == 'yes':
            curr_purch = Purchased.objects.get(user=request.user, course=Course.objects.get(id=int(classes_id)))
            curr_purch.add_prem_30days()
            curr_purch.save()
        elif _90days == 'yes':
            curr_purch = Purchased.objects.get(user=request.user, course=Course.objects.get(id=int(classes_id)))
            curr_purch.add_prem_90days()
            curr_purch.save()

        if prem == 'yes':
            request.user.is_premium = True
            request.user.save()
        else:
            request.user.is_premium = False
            request.user.save()
    
        test_purch = Purchased.objects.filter(user=request.user)

        for i in test_purch:
            print('prem: ' + str(
                self.assertFalse(i.has_prem())
            ) + ' ' + str(i) + ' ' + str(i.until))

        return redirect('classes_detail', klass_id=klass_id, dir_id=dir_id, sub_id=sub_id, classes_id=classes_id)


class KlassDetailView(View):

    def get(self, request, klass_id):
        klass_data = Course.objects.filter(klass=int(klass_id))

        return render(request, "main/klass_set.html", {"klass": klass_data,
                                                            "klass_id": klass_id
                                                            })


class DirDetailView(View):
    def get(self, request, klass_id, dir_id):
        # klass_data = Course.objects.filter(direction=dir_id, klass=klass_id)
        return render(request, "main/subject_chose.html", {
                                                           "klass_id": klass_id,
                                                           "dir_id": dir_id})
    """
        some_array = []
        final_array = []

        purchased_data = Purchased.objects.all()

        for i in purchased_data:
            if request.user == i.user:
                some_array.append(i)

        # if dir == rfm && klass == 2
        # klass_data = [urok 1, urok 2, urok 3]

        for j in klass_data:
            for y in some_array:
                if j == y.course:
                    final_array.append(j)

        return render(request, "main/dir_set.html", {"klass": klass_data,
                                                     "klass_id": klass_id,
                                                     "dir_id": dir_id,
                                                     "final_array": final_array})
    """
from django.forms.models import model_to_dict
from django.http import JsonResponse
class SubjectDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, klass_id, dir_id, sub_id):
        klass_data = Course.objects.filter(klass=klass_id, direction=dir_id, subject=sub_id)
        klass_data = klass_data.order_by('name')

        some_array = []
        final_array = []
        klass_data_clear = []
        purchased_data = []

        if request.user.is_authenticated:
            purchased_data = Purchased.objects.filter(user=request.user)

        for i in purchased_data:                #
            if request.user == i.user:          #это удалить и переделать
                some_array.append(i)            #

        for j in klass_data:
            for y in some_array:
                if j == y.course:
                    final_array.append(j)

        for i in klass_data:
            klass_data_clear.append(i)

        for i in final_array:
            for j in klass_data_clear:
                if i.id == j.id:
                    klass_data_clear.remove(i)

        if "test_start" in request.session:
            del request.session['test_start']

        """
        return render(request, "main/dir_set.html", {"klass": klass_data,
                                                     "klass_id": klass_id,
                                                     "dir_id": dir_id,
                                                     "sub_id": sub_id,
                                                     "final_array": final_array,
                                                     "klass_data_clear": klass_data_clear})
        """


        #return Response(data, status=status.HTTP_201_CREATED)

        current_purch = Purchased.objects.filter(user=request.user)

        queryset = klass_data.values()
        pp = current_purch.values()

        return Response({ 'kd': list(queryset),
                          'pp': list(pp)})


class CabinetMyLessView(View):
    global dir_choice 
    global sub_choice
    dir_choice = ['nis', 'ktl', 'rfm', '165']
    sub_choice = ["mat", "rus", "eng", "kaz"]
    #sub_choice = ["rus", "kaz", "eng", "mat"]


    def init_coockies(self, request):
        
        for i in range(12):
            if i == 0:
                continue
            else:
                request.session["klass%s" % i] = False

        for i in dir_choice:
            request.session[i] = False

        for i in sub_choice:
            request.session[i] = False

        request.session["klass_filter_settedb"] = False
        request.session["dir_filter_settedb"] = False
        request.session["sub_filter_settedb"] = False

    def get(self, request):
        
        if "first_enter" in request.session:
            if request.session.get("first_enter", True):
                self.init_coockies(request)
                request.session["first_enter"] = False
        else:
            request.session["first_enter"] = True
            return redirect("cabinet-myless")

        curr_purchases = []
        purchase_data = Purchased.objects.all()

        klass_filter = []
        dir_filter = []

        

        #check for unset filter for class
        default_filter = 0
        for i in range(12):
            if i == 0:
                continue
            else:
                s1 = 'klass%s' % i
                if s1 in request.session:
                    if request.session.get(s1, True):
                        break
                    else:
                        default_filter += 1


        if default_filter > 10:
            request.session["klass_filter_settedb"] = False
            for i in range(12):
                if i == 0:
                    continue
                else:
                    request.session["klass%s" % i] = True

        print("default_filter1 = " + str(default_filter))

        #check unset filter for direction
        default_filter = 0
        for i in dir_choice:
            if i in request.session:
                if request.session.get(i, True):
                    break
                else:
                    default_filter += 1

        print("default_filter2 = " + str(default_filter))

        if default_filter > 3:
            request.session["dir_filter_settedb"] = False
            for i in dir_choice:
                request.session[i] = True

        #check unset filter for subject
        default_filter = 0
        for i in sub_choice:
            if i in request.session:
                if request.session.get(i, True):
                    break
                else:
                    default_filter += 1

        if default_filter > 3:
            request.session["sub_filter_settedb"] = False
            for i in sub_choice:
                request.session[i] = True
        else:
            pass #sub_filter_settedb = True

        print("default_filter3 = " + str(default_filter))
        

        #print("klass_filter_settedb = " + str(klass_filter_settedb))
        #print("dir_filter_settedb = " + str(dir_filter_settedb))
        #print("sub_filter_settedb = " + str(sub_filter_settedb))

        if request.session.get("klass_filter_settedb", True) \
                or request.session.get("dir_filter_settedb", True) \
                or request.session.get("sub_filter_settedb", True):
            if len(Notification.objects.filter(user=request.user)) > 0:
                for j in Notification.objects.filter(user=request.user):
                    if j.notify_id == 1:
                        print("notify already set")
                    else:
                        notify = Notification(user=request.user, notify_id=1)
                        notify.save()
                        print("notify set")
            else:
                print("no notify find")
                notify = Notification(user=request.user, notify_id=1)
                notify.save()
                print("notify set")
        else:
            Notification.objects.filter(user=request.user, notify_id=1).delete()
            print("del notify from db")

        #check how many lessons have a user and use filter or not
        for i in purchase_data:
            if request.user == i.user:
                s1 = 'klass%s' % i.course.klass
                s2 = str(i.course.direction)
                s3 = str(i.course.subject)
                if s1 in request.session and s2 in request.session and s3 in request.session:
                    if request.session.get(s1 , True) and request.session.get(s2, True) \
                                                      and request.session.get(s3, True):
                        curr_purchases.append(i)

        all_notify = Notification.objects.filter(user=request.user)
        num_of_notify = len(all_notify)


        print("----")
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))


        return render(request, "main/cabinet-myless.html", {"curr_purchases": curr_purchases,
                                                            "all_notify": all_notify,
                                                            "num_of_notify": num_of_notify})

    def post(self, request):

        context = request.POST

        #set coockie for class filter 
        v_klass = []
        for i in range(12):
            if i == 0:
                continue
            else:
                v_klass.append(context.get('%s' % i))
    
        index = 1
        for i in v_klass:
            if i == 'yes':
                print("(post) v_klass %s" % index)
                request.session["klass%s" % index] = True
                request.session["klass_filter_settedb"] = True
            else:
                request.session["klass%s" % index] = False
            index += 1


        #set coockies for direction filter
        dir = [] 

        for i in dir_choice:
            dir.append(context.get(i))

        index = 0
        for i in dir:
            if i == 'yes':
                request.session[dir_choice[index]] = True
                request.session["dir_filter_settedb"] = True
            else:
                request.session[dir_choice[index]] = False
            index += 1


        #set coockies for subject filter
        subjects = [] 

        for i in sub_choice:
            subjects.append(context.get(i))

        index = 0
        for i in subjects:
            if i == 'yes':
                request.session[sub_choice[index]] = True
                request.session["sub_filter_settedb"] = True
            else:
                request.session[sub_choice[index]] = False
            index += 1

        for i in range(4):
            print("(post)" + sub_choice[i] + " " + str(subjects[i]))

        print(context)
        print("(post)----")
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))

        return redirect('cabinet-myless')


class CabinetView(View):
    def get(self, request):

        all_answers = Answer.objects.filter(user=request.user)
        right_answers = Answer.objects.filter(user=request.user, right=True)
        fall_answers = Answer.objects.filter(user=request.user, right=False)
        righti = 0
        falli = 0
        lvl = request.user.lvl
        exp = request.user.exp
        points = request.user.points

        if exp > lvl*10:
            lvl += 1
            request.user.lvl = lvl
            request.user.save()

        for i in right_answers:
            righti += 1

        for i in fall_answers:
            falli += 1
        
        for i in all_answers:
            print(i)

        return render(request, "main/cabinet.html", {"rights": righti,
                                                     "falls": falli,
                                                     "lvl": lvl,
                                                     "exp": exp,
                                                     "points": points})


    def post(self, request):
        context = request.POST
        clear_prems = context.get('clear_prems')

        if clear_prems == 'yes':
            purch = Purchased.objects.filter(user=request.user)
            for i in purch:
                if i.until is not None:
                    i.until = None
                    i.save()

        return redirect('cabinet')


# class RegistrationView(View):
    # def get(self, request):
    #    return render(request, "registration/reg.html")

def RegisterFunc(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/reg.html', {'user_form': user_form})


class BuyLessonView(View):
    def get(self, request, lesson_id):
        can_buy = True

        purchased_data = Purchased.objects.filter(user=request.user)
        lesson = Course.objects.filter(id=lesson_id)
        lesson = lesson[0]
        for i in purchased_data:
            if i == lesson_id:
                can_buy = False

        return render(request, "main/pre_buy.html", {"lesson_id": lesson_id,
                                                     "lesson": lesson,
                                                     "can_buy": can_buy})


def Buy(request, course_id):
    if request.method == 'POST':
        return render(request, "main/test.html", {"some_var":course_id})
    else:
        this_course = Course.objects.filter(id=course_id)
        this_course = this_course[0]
        new_purchase = Purchased(user=request.user,course=this_course)
        new_purchase.save()

        return render(request, "main/thx-for-buy.html", {"this_course": this_course})


class CSchoolRatingDetail(View):
    def get(self, request):
        print("WTF???")
        return render(request, "main/rating-detail.html")


class CSchoolRating(View):
    def get(self, request):
        return render(request, "main/rating.html")

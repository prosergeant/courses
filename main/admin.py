from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Purchased, Quest, Answer, Notification, QuizData, TestAnswers
from modeltranslation.admin import TranslationAdmin


# admin.site.register(Purchased)
# admin.site.register(Course)

admin.site.register(QuizData)
admin.site.register(Answer)
admin.site.register(Notification)
admin.site.register(TestAnswers)

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_display = ('course', 'course_klass', 'course_direction', 'course_subject',)
    list_filter = ('course',)
    class Media:
        js = ("main/js/quest.js",)

@admin.register(Purchased)
class PurchasedAdmin(admin.ModelAdmin):
    model = Purchased
    list_display = ('course', 'course_direction', 'course_klass', 'user',)
    list_filter = ('course',  'user',)


@admin.register(Course)
#class CourseAdmin(admin.ModelAdmin):
class CourseAdmin(TranslationAdmin):
    model = Course
    list_display = ('name', 'klass', 'subject', 'direction',)
    list_filter = ('name', 'klass', 'subject', 'direction',)
    class Media:
        js = ("main/js/course.js",)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'lvl', 'points',)
    list_filter = ('email', 'is_staff', 'is_active', 'points', 'lvl', 'exp',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone', 'first_time', 'points', 'lvl', 'exp', 'is_premium')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
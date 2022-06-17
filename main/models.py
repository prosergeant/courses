import datetime
import jwt
from datetime import date, timedelta
from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class Course(models.Model):
    name = models.CharField(help_text=_('Название'), verbose_name=_('name'), max_length=50)
    anons = models.CharField(help_text=_('Краткое описание'), verbose_name=_('anons'), max_length=50)
    video_file = models.FileField(upload_to="static/main/video_files", blank=True, null=True) #models.CharField('Видео', max_length=50)
    video_url = models.CharField(help_text=_('Видео url'), verbose_name=_('video_url'), max_length=250, blank=True, null=True)
    #pdf = models.CharField('PDF', max_length=50)
    quest = models.TextField(help_text=_('Текст задачи'), verbose_name=_('quest'))
    #content = HTMLField(blank=True, null=True)
    klass = models.IntegerField('Класс')


    DIR_CHOICES = [
        ('nis', 'НИШ'),
        ('ktl', 'КТЛ'),
        ('165', '165 Лицей'),
        ('rfm', 'РФМШ'),
    ]

    SUB_CHOICES = [
        ('rus', 'Русский'),
        ('kaz', 'Казахский'),
        ('eng', 'Английский'),
        ('mat', 'Математика'),
    ]

    direction = models.CharField('Направление', max_length=3, choices=DIR_CHOICES)
    subject = models.CharField('Предмет', max_length=3, choices=SUB_CHOICES)

    def __str__(self):
        return "%s (%s) (%s)" % (self.name, self.direction, self.klass)

    class Meta:
        verbose_name = _('course')  #"Курс"
        verbose_name_plural = _('courses')  #"Курсы"


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField("Номер телефона", max_length=20, blank=True)
    first_time = models.BooleanField(default=True)
    points = models.IntegerField(default=0)
    lvl =    models.IntegerField(default=1)
    exp =    models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.date.today() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Purchased(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    until = models.DateField(null=True, blank=True)

    def has_prem(self,current_date = datetime.date.today()):
        if self.until is None:
            return False
        
        return current_date < self.until

    def add_prem_7days(self, current_date = datetime.date.today()):
        _7days = timedelta(days=7)
        self.until = current_date + _7days

    def add_prem_30days(self, current_date = datetime.date.today()):
        _30days = timedelta(days=30)
        self.until = current_date + _30days

    def add_prem_90days(self, current_date = datetime.date.today()):
        _90days = timedelta(days=90)
        self.until = current_date + _90days

    @property
    def course_klass(self):
        return self.course.klass

    @property
    def course_direction(self):
        return self.course.direction

    def __str__(self):
        return "%s %s %s" % (self.course.name, self.course.klass, self.course.direction)


class Quest(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Questcourse")
    text = models.TextField('Вопрос',)
    var1 = models.TextField('Вариант 1', blank=True, null=True)
    var2 = models.TextField('Вариант 2', blank=True, null=True)
    var3 = models.TextField('Вариант 3', blank=True, null=True)

    """
    text = models.CharField('Вопрос', max_length=1024)
    var1 = models.CharField('Вариант 1', max_length=30, blank=True, null=True)
    var2 = models.CharField('Вариант 2', max_length=30, blank=True, null=True)
    var3 = models.CharField('Вариант 3', max_length=30, blank=True, null=True)
    """

    SUB_CHOICES = [
        ('var1', 'Вариант 1'),
        ('var2', 'Вариант 2'),
        ('var3', 'Вариант 3'),
    ]

    correct = models.CharField('Правильный ответ', max_length=4, choices=SUB_CHOICES, blank=True)

    def __str__(self):
        return self.course.name

    @property
    def course_klass(self):
        return self.course.klass

    @property
    def course_direction(self):
        return self.course.direction

    @property
    def course_subject(self):
        return self.course.subject


class Answer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    right = models.BooleanField(default=False)
    start = models.BooleanField(default=False)
    #right_answer = models.IntegerField(blank=True, null=True)


class Notification(models.Model):
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        # 0 - empty
        # 1 - my lessons filter is set
        notify_id = models.IntegerField(default=0)


class QuizData(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос")

    course_id = models.IntegerField(default=0)

    option_one = models.CharField(max_length=255, verbose_name="Правильный вариант")
    option_two = models.CharField(max_length=255, verbose_name="Вариант 2")
    option_three = models.CharField(max_length=255, verbose_name="Вариант 3")
    option_four = models.CharField(max_length=255, verbose_name="Вариант 4")

    #answer = models.CharField(max_length=255, verbose_name="Ответ")

    def __str__(self):
        return self.question


class TestAnswers(models.Model):
    user_id = models.IntegerField() #models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.IntegerField()
    course_obj = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    correct = models.IntegerField()
    all_answers = models.IntegerField()


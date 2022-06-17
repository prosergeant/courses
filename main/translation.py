from .models import Course
from modeltranslation.translator import register, TranslationOptions


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', "anons", "quest")
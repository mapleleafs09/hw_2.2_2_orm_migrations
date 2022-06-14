from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'

    object_list = Student.objects.order_by(ordering).prefetch_related('teacher')

    context = {'object_list' : object_list }


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)

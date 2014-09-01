__author__ = 'nicky'

from student.models import School

def get_school(**kwargs):
    name = School.objects.values("school_name")
    list = []
    for dict in name:
        for key in dict:
            list.append(dict[key])

    return list
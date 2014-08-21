from collections import defaultdict
from fs.errors import ResourceNotFoundError
import logging
import inspect

from path import path
from django.http import Http404
from django.conf import settings

from edxmako.shortcuts import render_to_string
from xmodule.modulestore import ModuleStoreEnum
from opaque_keys.edx.keys import CourseKey
from xmodule.modulestore.django import modulestore
from xmodule.contentstore.content import StaticContent
from xmodule.modulestore.exceptions import ItemNotFoundError
from static_replace import replace_static_urls
from xmodule.modulestore import ModuleStoreEnum
from xmodule.x_module import STUDENT_VIEW

from courseware.access import has_access
from courseware.model_data import FieldDataCache
from courseware.module_render import get_module
import branding

log = logging.getLogger(__name__)

def get_primary_course(courses, course_kinds):
    plist = []

    for course in courses:
        if course.get_course_kinds == course_kinds:
             if course.get_course_level == "Primary":
                 plist.append(course)

    return plist

def get_Intermediate_course(courses, course_kinds):

     mlist = []

     for course in courses:
        if course.get_course_kinds == course_kinds:
             if course.get_course_level == "Intermediate":
                 mlist.append(course)

     return mlist

def get_senior_course(courses, course_kinds):
    slist = []

    for course in courses:
        if course.get_course_kinds == course_kinds:
             if course.get_course_level == "Senior":
                 slist.append(course)

    return slist



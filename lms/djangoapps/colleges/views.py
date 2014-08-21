import logging
import urllib
import json

from collections import defaultdict
from django.utils.translation import ugettext as _

from django.conf import settings
from django.core.context_processors import csrf
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from edxmako.shortcuts import render_to_response, render_to_string
from django_future.csrf import ensure_csrf_cookie
from django.views.decorators.cache import cache_control
from django.db import transaction
from markupsafe import escape


from open_ended_grading import open_ended_notifications
from student.models import UserTestGroup, CourseEnrollment
from student.views import single_course_reverification_info
from util.cache import cache, cache_if_anonymous
from xblock.fragment import Fragment
from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import ItemNotFoundError, NoPathToItem
from xmodule.modulestore.search import path_to_location
from xmodule.tabs import CourseTabList, StaffGradingTab, PeerGradingTab, OpenEndedGradingTab
from xmodule.x_module import STUDENT_VIEW
import shoppingcart
from opaque_keys import InvalidKeyError

from microsite_configuration import microsite
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from instructor.enrollment import uses_shib
from courseware import grades
from courseware.access import has_access
from courseware.courses import get_courses, get_course, get_studio_url, get_course_with_access, sort_by_announcement
from courseware.category import get_primary_course, get_Intermediate_course, get_senior_course
from courseware.masquerade import setup_masquerade

log = logging.getLogger("edx.colleges")

template_imports = {'urllib': urllib}

CONTENT_DEPTH = 2

@ensure_csrf_cookie
@cache_if_anonymous
def colleges(request):

   courses = get_courses(request.user, request.META.get('HTTP_HOST'))
   return render_to_response("colleges/schools.html", {"courses": courses})


@ensure_csrf_cookie
@cache_if_anonymous
def jump_to(request, school_key_string):
    org = school_key_string
    course_list = []
    courses = get_courses(request.user, request.META.get('HTTP_HOST'))
    for course in courses:
        if course.display_org_with_default == org:
             course_list.append(course)
    return render_to_response("colleges/school_about.html", {
        "course_list": course_list,
        "org": org,
    })


def get_course_num(courses, school):
    num = 0
    for course in courses:
        if school == course.display_org_with_default:
            num += 1

    return num



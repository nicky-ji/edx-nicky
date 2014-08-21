
import json
import logging
from django.conf import settings
from django.db import models, IntegrityError
from importlib import import_module


log = logging.getLogger(__name__)
AUDIT_LOG = logging.getLogger("audit")
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

class School(models.Model):
    class Meta:
        db_table = "auth_school"

    school_name = models.CharField(max_length=255, db_index=True)

    """def get_meta(self):
        js_str = self.meta
        if not js_str:
            js_str = dict()
        else:
            js_str = json.loads(self.meta)

        return js_str"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import account
from .models import journal
from .models import transaction
from .models import ledger
from .models import journalEntry

# Register your models here.
admin.site.register(account)
admin.site.register(journal)
admin.site.register(transaction)
admin.site.register(ledger)
admin.site.register(journalEntry)

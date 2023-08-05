from django.contrib import admin
from .models import Manage
# Register your models here.

class manageAdmin(admin.ModelAdmin):
    list_display=("FIR_Number","Item_Name","IPC_Section","Crime_scene","Crime_date","Crime_time","Crime_witnesses","Crime_inspector","Item_status","where_its_kept")
    # list_editable = ("working","emp_id")
    # search_fields = ("name",)
    list_filter = ("Item_status","Crime_date")


admin.site.register(Manage,manageAdmin) 
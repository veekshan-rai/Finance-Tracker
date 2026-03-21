from django.contrib import admin
from .models import Transaction,Goals
from import_export import resources
from import_export.admin import ExportMixin

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ('date', 'title', 'amount', 'transaction', 'transaction_type')

class TransctionsAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TransactionResource
    list_display = ('date', 'title', 'amount', 'transaction_type')
    search_fields = ('title',)


admin.site.register(Transaction, TransctionsAdmin)
admin.site.register(Goals)


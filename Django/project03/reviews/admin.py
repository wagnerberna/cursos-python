from django.contrib import admin
from reviews.models import Reviews
from reviews.actions import approved_review, disapproved_review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "review", "approved"]
    actions = [approved_review, disapproved_review]


admin.site.register(Reviews, ReviewAdmin)

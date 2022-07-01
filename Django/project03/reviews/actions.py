def approved_review(modelamin, request, queryset):
    queryset.update(approved=True)


def disapproved_review(modelamin, request, queryset):
    queryset.update(approved=False)


approved_review.short_description = "Aprova comentário"
disapproved_review.short_description = "Reprova comentário"

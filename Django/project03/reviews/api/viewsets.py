from rest_framework import viewsets
from reviews.models import Reviews
from reviews.api.serializers import ReviewsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

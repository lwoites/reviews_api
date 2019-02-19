
from rest_framework import generics, permissions

from consumeraffairs.reviews.models import Company, Review
from consumeraffairs.reviews.serializers import CompanySerializer, ReviewSerializer
from consumeraffairs.reviews.permissions import IsReviewer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated, IsReviewer,)

    def get_queryset(self):
        return Review.objects.filter(reviewer=self.request.user)



class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

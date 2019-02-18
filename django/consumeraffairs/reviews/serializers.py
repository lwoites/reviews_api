from rest_framework import serializers

from consumeraffairs.reviews.models import Company, Review


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description')


class ReviewSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'summary', 'rating', 'created', 'reviewer_ip', 'company')
        read_only_fields = ('reviewer_ip',' company')


    def create(self, validated_data):
        request = self.context.get('request')
        user_ip = request.META.get('REMOTE_ADDR')

        review = Review(**validated_data)
        review.reviewer_ip = user_ip
        review.save()

        return review


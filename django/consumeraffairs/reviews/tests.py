
from model_mommy import mommy

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase

from consumeraffairs.reviews.models import Review, Company
from consumeraffairs.users.models import Reviewer


class ReviewTests(APITestCase):
    
    def setUp(self):
        self.password = "user_1"
        self.user = Reviewer.objects.create_user("user_1", "user_1@example.com", self.password)
        self.company = mommy.make(Company, name="ACME", description="A Wonderful Company")

    def login(self,):
        self.client.login(username=self.user.username, password=self.password)

    def test_get_reviews_when_non_authenticated_user(self):
        url = reverse('review-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_reviews_when_theres_no_reviews(self):
        self.login()
        url = reverse('review-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 0)
        self.assertEqual(response.data.get('results'), [])

    def test_create_review(self):
        before_count = Review.objects.all().count()

        self.login()

        response = self.client.post(reverse('review-list'), self.get_review_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(before_count + 1, Review.objects.all().count())
        review = Review.objects.last()
        self.assertEqual(review.title, 'Fantastic Hammer')
        self.assertEqual(review.summary, 'The ACME Fantastic Hammer is really fantastic')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.reviewer, self.user)
        self.assertEqual(review.company, self.company)

    def test_get_reviews(self):
        self.login()
        url = reverse('review-list')
        
        # creates one review
        response = self.client.post(url, self.get_review_data())
        review_pk = response.data.get('id')
        # gets all reviews
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)
        
        self.assertEqual(len(response.data.get('results')), 1)
        self.assertEqual(response.data.get('results')[0]['id'], review_pk)

    def test_dont_get_other_user_reviews(self):
        user_2 = mommy.make(Reviewer, username='user_2')
        mommy.make(Review, reviewer=user_2)
        mommy.make(Review, reviewer=user_2)
        user_1_reviews = [
            mommy.make(Review, reviewer=self.user),
            mommy.make(Review, reviewer=self.user),
            mommy.make(Review, reviewer=self.user),
        ]

        self.login()
        url = reverse('review-list')
        response = self.client.get(url)
        self.assertEqual(response.data.get('count'), len(user_1_reviews))
        for review, returned_review in zip(user_1_reviews, response.data.get('results')):
            self.assertEqual(returned_review['id'], review.pk)

    def test_get_review_details(self):
        url = lambda pk: reverse('review-details', kwargs={'pk': pk})
        review = mommy.make(Review, reviewer=self.user)

        self.login()
        response = self.client.get(url(review.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        self.assertEqual(response.data['id'], review.id)

    def test_dont_get_other_user_review_details(self):
        url = lambda pk: reverse('review-details', kwargs={'pk': pk})
        user_2 = mommy.make(Reviewer, username="user_2")
        review = mommy.make(Review, reviewer=user_2)

        self.login()
        response = self.client.get(url(review.pk))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 
        
    def get_review_data(self):
        return {
            'title': 'Fantastic Hammer',
            'summary': 'The ACME Fantastic Hammer is really fantastic',
            'rating': 5,
            'company': self.company.pk
        }


class CompanyModelsTest(TestCase):

    def test_company_str(self):
        company = mommy.make(Company, name='ACME') 
        self.assertEqual(str(company), 'ACME')


class ReviewModelsTest(TestCase):

    def test_review_str(self):
        review = mommy.make(Review, title='review 1') 
        self.assertEqual(str(review), 'review 1')

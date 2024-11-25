import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from ads.models import Ad, Review
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create(
        email='testuser@test.ru',
        password='testpassword',
        first_name='test',
        last_name='testov'
    )


@pytest.fixture
def admin_user():
    return User.objects.create(
        email='adminuser@test.ru',
        password='adminpassword',
        first_name='admin',
        last_name='adminov',
        is_admin=True
    )


@pytest.fixture
def ad(user):
    return Ad.objects.create(
        title='Test Ad',
        description='Test Description',
        author=user
    )


@pytest.fixture
def review(user, ad):
    return Review.objects.create(
        text='Test Review',
        ad=ad,
        author=user
    )


@pytest.mark.django_db
class TestAdAPI:

    def test_ad_list(self, api_client):
        url = reverse('ads:ad_list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_ad_create(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse('ads:ad_create')
        data = {'title': 'New Ad', 'description': 'New Description'}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Ad.objects.count() == 1

    def test_ad_create_not_authenticate(self, api_client, user):
        url = reverse('ads:ad_create')
        data = {'title': 'New Ad', 'description': 'New Description'}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Ad.objects.count() == 0

    def test_ad_retrieve(self, api_client, user, ad):
        api_client.force_authenticate(user=user)
        url = reverse('ads:ad_get', args=[ad.pk])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_ad_update(self, api_client, ad, user):
        api_client.force_authenticate(user=user)
        url = reverse('ads:ad_update', args=[ad.pk])
        data = {'title': 'Updated Ad', 'description': 'Updated Description'}
        response = api_client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        ad.refresh_from_db()
        assert ad.title == 'Updated Ad'

    def test_ad_destroy(self, api_client, ad, user):
        api_client.force_authenticate(user=user)
        url = reverse('ads:ad_delete', args=[ad.pk])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Ad.objects.count() == 0


@pytest.mark.django_db
class TestReviewAPI:

    def test_review_list(self, api_client, user, ad):
        api_client.force_authenticate(user=user)
        url = reverse('ads:review_list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_review_create(self, api_client, user, ad):
        api_client.force_authenticate(user=user)
        url = reverse('ads:review_create')
        data = {'text': 'New Review', 'ad': ad.pk}
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Review.objects.count() == 1

    def test_review_retrieve(self, api_client, user, review):
        api_client.force_authenticate(user=user)
        url = reverse('ads:review_get', args=[review.pk])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_review_update(self, api_client, review, user):
        api_client.force_authenticate(user=user)
        url = reverse('ads:review_update', args=[review.pk])
        data = {'text': 'Updated Review'}
        response = api_client.patch(url, data)

        assert response.status_code == status.HTTP_200_OK
        review.refresh_from_db()
        assert review.text == 'Updated Review'

    def test_review_destroy(self, api_client, review, user):
        api_client.force_authenticate(user=user)
        url = reverse('ads:review_delete', args=[review.pk])
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Review.objects.count() == 0

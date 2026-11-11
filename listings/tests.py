from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from listings.models import Listing


class AccountFlowTests(TestCase):
    def test_signup_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse("signup_view"),
            {
                "username": "new-user",
                "email": "new@example.com",
                "password": "a-strong-password-123",
                "password2": "a-strong-password-123",
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="new-user").exists())
        self.assertIn("_auth_user_id", self.client.session)


class ListingAccessTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner",
            password="owner-password-123",
        )
        self.other_user = User.objects.create_user(
            username="other",
            password="other-password-123",
        )
        self.listing = Listing.objects.create(
            title="Used bike",
            description="A bike in good condition",
            price="125.00",
            image=SimpleUploadedFile(
                "bike.jpg",
                b"not-a-real-image",
                content_type="image/jpeg",
            ),
            owner=self.owner,
        )

    def tearDown(self):
        if self.listing.image:
            self.listing.image.delete(save=False)
        super().tearDown()

    def test_user_listings_only_contains_the_signed_in_users_listings(self):
        other_listing = Listing.objects.create(
            title="Other item",
            description="Not owned by the first user",
            price="50.00",
            image=SimpleUploadedFile(
                "other.jpg",
                b"not-a-real-image",
                content_type="image/jpeg",
            ),
            owner=self.other_user,
        )
        self.addCleanup(lambda: other_listing.image.delete(save=False))

        self.client.login(username="owner", password="owner-password-123")
        response = self.client.get(reverse("listings:userListings"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Used bike")
        self.assertNotContains(response, "Other item")

    def test_user_cannot_edit_another_users_listing(self):
        self.client.login(username="other", password="other-password-123")

        response = self.client.post(
            reverse("listings:editListing", args=[self.listing.id]),
            {"title": "Changed title", "description": "Changed", "price": "1.00"},
        )

        self.assertEqual(response.status_code, 404)
        self.listing.refresh_from_db()
        self.assertEqual(self.listing.title, "Used bike")

    def test_search_matches_description(self):
        response = self.client.post(
            reverse("listings:allListings"),
            {"keyWord": "condition"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Used bike")

from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""

        email = "test@testuser.com"
        password = "some-str-pass-123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email of a new registered user is normalized."""

        email = "test@YAHOO.COM"
        user = get_user_model().objects.create_user(email, "test-12345")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test-12345")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        superuser = get_user_model().objects.create_superuser(
            "admin@test.org",
            "test-12345",
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

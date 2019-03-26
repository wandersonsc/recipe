import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer

User = get_user_model()


class TestModel:
    """
    Test creating a new user using an email
    """

    def test_create_user_with_email(self, db):
        email = 'admin@admin.com'
        password = 'asd123456'
        user = User.objects.create_user(
            email=email,
            password=password
        )
        assert user.pk == 1, 'Should return true is the user was created'
        assert user.email == email
        assert user.check_password(password) is True

    def test_new_user_email_normalized(self, db):
        email = 'admin@ADMIN.com'
        password = 'asd123456'
        user = User.objects.create_user(
            email=email,
            password=password
        )
        assert user.email == email.lower()

    def test_new_user_invalid_email(self, db):
        """
        Test creating using with no given user
        """
        with pytest.raises(ValueError):
            User.objects.create_user(None, '123456ss')

    def test_create_super_user(self, db):
        """
        Test creating a new superuser
        """
        email = 'admin@admin.com'
        password = 'asd123456'
        user = User.objects.create_superuser(
            email=email,
            password=password
        )
        assert user.is_superuser is True
        assert user.is_staff is True

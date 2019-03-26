from django.conf import settings


class TestInstalledApp:

    def test_installed_app(self):
        assert "accounts" in settings.INSTALLED_APPS

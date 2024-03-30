from django.apps import AppConfig


class BewellBlogConfig(AppConfig):
    """
    Provides primary key type for bewell_blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bewell_blog'

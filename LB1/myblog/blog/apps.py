from django.apps import AppConfig


class BlogConfig(AppConfig): #клас конфігурації котрий автоматично створюється при створенні додатку
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

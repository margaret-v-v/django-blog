# Generated by Django 3.2.18 on 2023-04-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_body_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image', verbose_name='Зображення'),
            preserve_default=False,
        ),
    ]

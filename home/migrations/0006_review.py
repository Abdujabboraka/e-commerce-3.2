# Generated by Django 5.1.2 on 2024-11-01 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_category_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='Matn')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='manzil')),
                ('author_photo', models.ImageField(blank=True, null=True, upload_to='user-avatar/', verbose_name='avatar')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='avtor')),
            ],
            options={
                'verbose_name': 'Sharx',
                'verbose_name_plural': 'Sharxlar',
            },
        ),
    ]
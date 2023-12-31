# Generated by Django 4.2.1 on 2023-05-30 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(null=True, verbose_name='Примечание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='resources', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Ресурс',
                'verbose_name_plural': 'Ресурсы',
                'ordering': ['pub_date'],
            },
        ),
    ]

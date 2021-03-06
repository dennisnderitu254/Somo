# Generated by Django 2.2.1 on 2019-07-05 14:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(choices=[('Dr.', 'Doctor'), ('Prof.', 'Professor'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], help_text="Instructor's Salutation", max_length=16)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Course', verbose_name='course id')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Instructor', verbose_name='instructor id')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Instructor', verbose_name='instructor'),
        ),
    ]

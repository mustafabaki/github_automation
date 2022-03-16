# Generated by Django 4.0.3 on 2022-03-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('html_url', models.CharField(max_length=100)),
                ('avatar_url', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('hireable', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=100)),
                ('repos', models.CharField(max_length=100)),
                ('followers', models.CharField(max_length=100)),
            ],
        ),
    ]
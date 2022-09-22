# Generated by Django 4.1.1 on 2022-09-20 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_app.project')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-12 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippet_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='snippet',
        ),
        migrations.AddField(
            model_name='snippet',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snippet_app.tag'),
        ),
    ]

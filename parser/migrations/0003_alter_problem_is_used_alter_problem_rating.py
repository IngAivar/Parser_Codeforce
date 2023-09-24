# Generated by Django 4.2.4 on 2023-09-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_alter_problem_is_used_alter_problem_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='Is_used'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rating'),
        ),
    ]
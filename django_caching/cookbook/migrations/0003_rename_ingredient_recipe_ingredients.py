# Generated by Django 4.2.15 on 2024-09-03 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_remove_recipe_ingredient_recipe_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-23 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_ideaitem_idea_ideaitem_content_ideaitem_title_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IdeaItem',
            new_name='Idea',
        ),
    ]

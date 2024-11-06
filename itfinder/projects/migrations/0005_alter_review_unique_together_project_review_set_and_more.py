# Generated by Django 4.0.6 on 2024-10-31 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_review_text_review_body_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='project',
            name='review_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.review'),
        ),
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
    ]

# Generated by Django 4.0.6 on 2024-10-26 10:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('total_votes', models.IntegerField(blank=True, default=0, null=True)),
                ('votes_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=500, null=True)),
                ('source_link', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_text', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.tag'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insert_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('deleted', models.IntegerField()),
                ('published', models.IntegerField()),
                ('museum_int_id', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('museum', models.CharField(blank=True, max_length=100, null=True)),
                ('museum_url', models.CharField(blank=True, max_length=300, null=True)),
                ('date_human', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.CharField(blank=True, max_length=10, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('technique_material', models.CharField(blank=True, max_length=200, null=True)),
                ('acquisition', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('inscription', models.TextField(blank=True, null=True)),
                ('material', models.CharField(blank=True, max_length=300, null=True)),
                ('creator', models.CharField(blank=True, max_length=100, null=True)),
                ('signature', models.CharField(blank=True, max_length=200, null=True)),
                ('exhibitions', models.CharField(blank=True, max_length=300, null=True)),
                ('literature', models.CharField(blank=True, max_length=300, null=True)),
                ('reproductions', models.CharField(blank=True, max_length=300, null=True)),
                ('bundle', models.CharField(blank=True, max_length=50, null=True)),
                ('bundle_order', models.PositiveIntegerField(blank=True, null=True)),
                ('bundle_side', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'artwork',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('page', models.IntegerField(blank=True, null=True)),
                ('pageid', models.CharField(blank=True, max_length=20, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('side', models.CharField(blank=True, max_length=20, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('birth_year', models.CharField(blank=True, max_length=4, null=True)),
                ('death_year', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
    ]

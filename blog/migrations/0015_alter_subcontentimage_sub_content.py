# Generated by Django 4.1.4 on 2023-04-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_view_delete_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcontentimage',
            name='sub_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subcontent'),
        ),
    ]

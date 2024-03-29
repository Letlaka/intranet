# Generated by Django 5.0.1 on 2024-03-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intra_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='document',
            name='under_review',
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('under_review', 'Under Review'), ('approved', 'Approved')], default='pending', help_text='Status of the document.', max_length=20),
        ),
        migrations.AlterField(
            model_name='document',
            name='council_resolution_number',
            field=models.CharField(blank=True, help_text='Council resolution number associated with the document.', max_length=255, null=True),
        ),
    ]

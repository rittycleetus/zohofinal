# Generated by Django 3.2.25 on 2024-05-31 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_delete_bill_comments1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill_history',
            old_name='company',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='bill_history',
            old_name='login_details',
            new_name='Login_Details',
        ),
        migrations.RenameField(
            model_name='bill_reference',
            old_name='company',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='bill_reference',
            old_name='login_details',
            new_name='Login_Details',
        ),
    ]

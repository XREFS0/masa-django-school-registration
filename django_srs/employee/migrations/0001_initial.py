"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeInfo",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("register_number", models.CharField(max_length=20)),
                ("register_date", models.DateField()),
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("another_name", models.CharField(max_length=100)),
                ("nid", models.IntegerField()),
                ("employee_photo", models.ImageField(upload_to="photos/%Y/%m/%d/")),
            ],
        ),
    ]

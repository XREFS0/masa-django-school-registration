"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("status", models.IntegerField(default=0)),
                (
                    "student",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="students.StudentInfo"),
                ),
            ],
        ),
    ]

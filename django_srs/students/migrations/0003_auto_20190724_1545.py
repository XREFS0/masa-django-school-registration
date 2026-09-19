"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_attendance"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="studentinfo",
            unique_together={("admission_id", "class_type")},
        ),
    ]

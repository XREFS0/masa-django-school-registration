"""
Developed by MASA
All Rights Reserved.
"""

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_auto_20190724_1545"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="attendance",
            unique_together={("student", "date")},
        ),
    ]

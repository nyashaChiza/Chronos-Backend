# Generated by Django 4.2.2 on 2023-07-02 08:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0019_evaluationinvite_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

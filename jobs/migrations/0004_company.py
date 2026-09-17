from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_notice_period'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'company_name',
                    models.CharField(
                        max_length=200,
                        unique=True,
                    ),
                ),
                (
                    'location',
                    models.CharField(
                        blank=True,
                        max_length=200,
                    ),
                ),
                (
                    'website',
                    models.URLField(
                        blank=True,
                    ),
                ),
                (
                    'description',
                    models.TextField(
                        blank=True,
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True,
                    ),
                ),
                (
                    'created_by',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
    ]
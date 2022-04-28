from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations, models
import django.db.models.deletion
import logging


logger = logging.getLogger(__name__)

role_permissions = {
    'Dog Owners': [
       'Can view profile',
       'Can delete profile',
       'Can add profile',
       'Can change profile',
    ],
}


# See https://code.djangoproject.com/ticket/23422
def add_role_permissions(apps, schema_editor):
    emit_post_migrate_signal(2, False, 'default')

    for r in role_permissions:
        role, created = Group.objects.get_or_create(name=r)
        for p in role_permissions[r]:
            perm, created2 = Permission.objects.get_or_create(name=p)
            role.permissions.add(perm)
        role.save()


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '__latest__'),
        ('auth', '__latest__'),
        ('myapp', '0003_add_default_groups'),
    ]

    operations = [
        migrations.RunPython(add_role_permissions),
    ]

# Users don't have perms to start unless superuser
# Signals => post_save() runs before completely saving object
# Custom migrations - use of __latest__
# Groups can have permissions and be attached to Users, User can also have single perms
# SITE_ID
# Permissions model
# Using shell to debug
# migrations.RunPython for seeding a DB maybe.
# Only is_staff can use Django admin. Could add is_staff as Boolean field and default to true
# get_or_create()
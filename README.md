# Python-Migration-To-Unique-UUID-Field
- Applying a “plain” migration that adds a unique non-nullable field to a table with existing rows will raise an error because the value used to populate existing rows is generated only once, thus breaking the unique constraint.

- Therefore, the following steps should be taken. In this example, we’ll add a non-nullable **UUIDField** with a default value. Modify the respective field according to your needs.

- Add the field on your model with default=uuid.uuid4 and unique=True arguments (choose an appropriate default for the type of the field you’re adding).

- Run the makemigrations command. This should generate a migration with an AddField operation.

- Generate two empty migration files for the same app by running makemigrations myapp --empty twice. We’ve renamed the migration files to give them meaningful names in the examples below.

- Copy the AddField operation from the auto-generated migration (the first of the three new files) to the last migration, change AddField to AlterField, and add imports of uuid and models. For example:


'from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
'
- Edit the first migration file. The generated migration class should look similar to this:

'class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150129_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
'

Change unique=True to null=True – this will create the intermediary null field and defer creating the unique constraint until we’ve populated unique values on all the rows.

- In the first empty migration file, add a RunPython or RunSQL operation to generate a unique value (UUID in the example) for each existing row. Also add an import of uuid. For example:

'from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('myapp', 'MyModel')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_add_uuid_field'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
'

- Now you can apply the migrations as usual with the migrate command.

Note there is a race condition if you allow objects to be created while this migration is running. Objects created after the AddField and before RunPython will have their original uuid’s overwritten.
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        # ('product', '0002_auto_20210218_0155'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bagmodel',
            name='video',
        ),
    ]
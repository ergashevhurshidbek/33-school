# Generated by Django 3.2.9 on 2021-12-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoMessageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptio', models.TextField(verbose_name='Izoh')),
                ('shortDescription', models.TextField(verbose_name='Qisqa Izoh')),
                ('video', models.FileField(upload_to='media/video', verbose_name='media')),
            ],
        ),
        migrations.AlterField(
            model_name='employes',
            name='fullName',
            field=models.TextField(max_length=200, verbose_name='Ism Familiya'),
        ),
        migrations.AlterField(
            model_name='employes',
            name='proffession',
            field=models.TextField(max_length=200, verbose_name='Fan turi'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=1024, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='Ism Familiya'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name='Xabar'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Bayonat'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='thingcounts',
            name='rooms',
            field=models.CharField(max_length=100000, verbose_name='Xonalar soni'),
        ),
        migrations.AlterField(
            model_name='thingcounts',
            name='students',
            field=models.CharField(max_length=100000, verbose_name="O'quvchilar soni"),
        ),
        migrations.AlterField(
            model_name='thingcounts',
            name='teachers',
            field=models.CharField(max_length=100000, verbose_name="O'qituvchilar soni"),
        ),
    ]
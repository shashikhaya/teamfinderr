# Generated by Django 3.1.7 on 2021-04-08 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategoryMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('relationship', 'Relationship'), ('communication', 'Communication'), ('management', 'Management'), ('analytical', 'Analytical'), ('creative', 'Creative'), ('technical', 'Technical')], max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skillcategorymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.skillcategorymixin')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('profiles.skillcategorymixin',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, related_name='profile', to='profiles.Skill')),
            ],
        ),
    ]

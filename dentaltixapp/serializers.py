"""Serializers for model"""
from django.utils.encoding import smart_text
from rest_framework import serializers
from dentaltixapp.models import ProgrammingLanguage, Framework
from django.core.exceptions import ObjectDoesNotExist


class ExtendSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    # Representation of relathionship. It uses function __unicode__
    frameworks = ExtendSlugRelatedField(many=True, slug_field='name', allow_null=True, queryset=Framework.objects.all())

    class Meta:
        model = ProgrammingLanguage
        fields = ('name', 'frameworks')


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = ('name')

import django_filters # type: ignore
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner', 'image', 'salary', 'vacancy', 'excperience', 'responsibility', 'slug', 'qualifications', 'benefits', 'published_at']
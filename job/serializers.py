from rest_framework import serializers
from .models import Job, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)  # Only include the 'name' field


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields = ['owner','title','description','job_type','vacancy','salary','category','excperience','responsibility','qualifications','benefits','image','published_at']

    def get_owner(self, obj):
        return obj.owner.first_name
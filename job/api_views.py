from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Job
from .serializers import JobSerializer
from .permission import CanAccessJob

class JobListApi(generics.ListAPIView):
    queryset = Job.objects.all().order_by('published_at')
    serializer_class = JobSerializer

class JobCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class JobDetailList(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'slug'  # Use 'slug' as the lookup field

    def get_object(self):
        queryset = self.get_queryset()
        # Fetch the job using the slug
        obj = generics.get_object_or_404(queryset, slug=self.kwargs['slug'])
        return obj

class JobDetailUpdate(APIView):
    permission_classes = [IsAuthenticated]  # Set default permission

    def get_object(self, slug):
        try:
            return Job.objects.get(slug=slug)
        except Job.DoesNotExist:
            return None

    def get(self, request, slug, format=None):
        job = self.get_object(slug)
        if job is None:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        job = self.get_object(slug)
        if job is None:
            return Response(status=HTTP_404_NOT_FOUND)

        # Permission check for update (ownership check or custom logic)
        if not (job.owner == request.user or request.user.has_perm('jobs.change_job', job)):
            return Response({'error': 'You are not authorized to update this job.'}, status=HTTP_403_FORBIDDEN)

        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class JobDelete(APIView):
    permission_classes = [IsAuthenticated]  # Set default permission

    def get_object(self, slug):
        try:
            return Job.objects.get(slug=slug)
        except Job.DoesNotExist:
            return None

    def delete(self, request, slug, format=None):
        job = self.get_object(slug)
        if job is None:
            return Response(status=HTTP_404_NOT_FOUND)

        # Permission check for delete (ownership check or custom logic)
        if not (job.owner == request.user or request.user.has_perm('jobs.delete_job', job)):
            return Response({'error': 'You are not authorized to delete this job.'}, status=HTTP_403_FORBIDDEN)

        job.delete()
        return Response(status=HTTP_204_NO_CONTENT)





    
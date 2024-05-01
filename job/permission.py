from rest_framework.permissions import BasePermission

class CanAccessJob(BasePermission):
    """
    Custom permission to access or modify a job.
    """

    def has_permission(self, request, view, obj):
        # Define your permission logic here (e.g., ownership check)
        if request.method in ('PUT', 'DELETE'):
            return obj.owner == request.user  # Allow if user owns the job for update/delete
        return True  # Allow GET requests for all users
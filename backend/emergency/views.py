from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils.timezone import now
from .models import Emergency
from .serializers import EmergencySerializer
from rest_framework.exceptions import PermissionDenied
class EmergencyViewSet(ModelViewSet):
    serializer_class = EmergencySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'citizen':
            return Emergency.objects.filter(user=user)

        elif user.role == 'volunteer':
            return Emergency.objects.filter(
                status='pending',
                assigned_to__isnull=True
            )

        elif user.role == 'authority':
            return Emergency.objects.filter(
                status__in=['pending', 'assigned']
            ).order_by('-created_at')

        return Emergency.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != 'citizen':
            raise PermissionDenied("Only citizens can create emergencies")

        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        if request.user.role != 'volunteer':
            return Response({"error": "Only volunteers allowed"}, status=403)

        try:
            with transaction.atomic():
                emergency = Emergency.objects.select_for_update().get(pk=pk)

                if emergency.assigned_to:
                    return Response({"error": "Already assigned"}, status=400)

                if emergency.status != 'pending':
                    return Response({"error": "Not available"}, status=400)

                emergency.assigned_to = request.user
                emergency.status = 'assigned'
                emergency.assigned_at = now()
                emergency.save()

                return Response({"message": "Assigned successfully"})

        except Emergency.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

    # 🔴 UPDATE STATUS
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        if request.user.role != 'authority':
            return Response({"error": "Only authority allowed"}, status=403)

        try:
            emergency = Emergency.objects.get(pk=pk)
        except Emergency.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        new_status = request.data.get("status")

        valid_transitions = {
            'pending': ['assigned'],
            'assigned': ['resolved'],
            'resolved': []
        }

        if new_status not in valid_transitions[emergency.status]:
            return Response({"error": "Invalid transition"}, status=400)

        emergency.status = new_status

        if new_status == 'resolved':
            emergency.resolved_at = now()

        emergency.save()

        return Response({"message": "Status updated"})
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwner
from .selectors import get_user_notes
from .services import create_note


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return get_user_notes(user=self.request.user)

    def perform_create(self, serializer):
        create_note(
            user=self.request.user,
            title=serializer.validated_data["title"],
            content=serializer.validated_data["content"],
        )

from .models import Note


def get_user_notes(*, user):
    return Note.objects.filter(user=user)


def get_user_note_by_id(*, user, note_id: int):
    return Note.objects.get(id=note_id, user=user)

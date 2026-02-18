from .models import Note


def create_note(*, user, title: str, content: str) -> Note:
    return Note.objects.create(
        user=user,
        title=title,
        content=content
    )

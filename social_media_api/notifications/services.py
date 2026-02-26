from typing import Any
from .models import Notification

def create_notification(*, recipient, actor, verb: str, target: Any = None):
    if recipient == actor:
        return None
    
    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target=target,
    )
from datetime import datetime

from app.logging.logger import logger


def log_event(
    event_type: str,
    agent_id: str,
    details: dict
):

    logger.info({
        "timestamp": datetime.utcnow().isoformat(),
        "agent_id": agent_id,
        "event_type": event_type,
        "details": details
    })
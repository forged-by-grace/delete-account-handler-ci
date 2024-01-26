from passlib.context import CryptContext

from core.event.produce_event import produce_event

from core.utils.settings import settings
from core.model.account_model import AccountID
from core.utils.init_log import logger


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
async def delete_account(id: str) -> None:
    # Create delete account obj
    delete_obj = AccountID(id=id)

    # Serialize
    delete_account_event = delete_obj.serialize()

    # Emit event
    logger.info('Emitting delete account event.')
    await produce_event(topic=settings.api_delete_account, value=delete_account_event)
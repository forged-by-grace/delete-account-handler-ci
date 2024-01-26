from core.helper.consumer_helper import consume_event
from core.model.account_model import AccountID
from core.utils.settings import settings
from core.helper.account_helper import delete_account
from core.utils.init_log import logger


async def consume_delete_account_event():
    # consume event
    consumer = await consume_event(topic=settings.api_delete_account_topic, group_id=settings.api_delete_account_topic)
    
    try:
        # Consume messages
        async for msg in consumer:  
            logger.info('Received delete account event.')          
            # Deserialize event
            account_data = AccountID.deserialize(data=msg.value)

            # Delete account
            logger.info('Deleting account.')
            await delete_account(id=account_data.id)
            
    except Exception as err:
        logger.error(f'Failed to delete account with error: {str(err)}')
    finally:
        logger.warning('Consumer is stopping.')
        await consumer.stop()

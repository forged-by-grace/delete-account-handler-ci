from core.connection.db_connection import account_col

from core.model.account_model import AccountInDB

from pydantic import EmailStr


async def get_account_by_email(email: EmailStr):
    """    
    This is used to retrieve an account from the database using email.
    @params {email} - The email registered to the account to be retrieved.
    @returns {object} - A dict containing the account data
    
    """
    
    # Filter
    filter = {"email": email}

    # Query
    response = await account_col.find_one(filter=filter)

    # Check if response is None
    if not response:
        return None
    
    # Deserialize
    account_obj = AccountInDB(**response)

    return account_obj


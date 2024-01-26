from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Event Streaming Server
    api_event_streaming_host:str
    api_event_streaming_client_id: str

    # Service metadata
    service_name: str

    # Streaming topics    
    api_delete_account: str    
    api_delete_account_topic: str
    
    # API model versions
    account_model_version: int

    # Cache credentials   
    api_redis_host_local: str    
   
    # DB credentials
    api_db_url: str

    
settings = Settings()

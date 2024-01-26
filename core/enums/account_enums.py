from enum import Enum

class NotificationChannel(str, Enum):
    email='email'
    sms='sms'
    call='call'
    push_notification='push notification'

class NotificationTemplate(str, Enum):
     email_verification = "email_verification"
     phone_verification='Phone_verification'
     forgot_password='Forgot_password'
     reset_password='Reset_password'
     new_account_registration='new_account_registration'
     transaction_verification='Transaction_verification'
    
class OTPPurpose(str, Enum):
     email_verification='Email verification'
     phone_verification='Phone verification'
     forgot_password='Forgot password'
     reset_password='Reset password'
     transaction_verification='Transaction verification'

class Role(str, Enum):
    anonymouse = "anonymous"    
    authenticated = "authenticated"
    admin = "admin"



from pydantic import BaseModel, EmailStr, Field, field_validator, validator
from database import accounts_validators
import re


class UserRegistrationRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserActivationRequestSchema(BaseModel):
    email: EmailStr
    token: str = Field(..., min_length=1)


class PasswordResetRequestSchema(BaseModel):
    email: EmailStr


class PasswordResetCompleteRequestSchema(BaseModel):
    email: EmailStr
    token: str = Field(..., min_length=1)
    password: str = Field(..., min_length=8, max_length=128)


class UserLoginResponseSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserLoginRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class TokenRefreshResponseSchema(BaseModel):
    token: str = Field(..., min_length=1)


class TokenRefreshRequestSchema(BaseModel):
    refresh_token: str = Field(..., min_length=1)


class UserRegistrationResponseSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class MessageResponseSchema(BaseModel):
    message: str


class TokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "bearer"

from pydantic import BaseModel, Field, EmailStr, ValidationError

class Account(BaseModel):
    name: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=9, pattern=r'^(?=.*[A-Z])(?=.*\d).+$')
try:
    account = Account(name="Jn", email="johnexample.com", password="a1xxxxxxx")
    print(account)
except ValidationError as err:
    print(err)
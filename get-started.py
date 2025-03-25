from pydantic import BaseModel, field_validator, EmailStr, ValidationError
from pydantic import EmailStr

# Define UserProfile model
class UserProfile(BaseModel):
    name: str
    age: int = 18  # Default value
    email: EmailStr  # Using EmailStr for email validation
    is_active: bool = True  # Default value

try:
    user_invalid_email = UserProfile(name="Tuyen ", age=18, email="tuyen@example.com")
    print(user_invalid_email)
except ValidationError as e:
    print(f"Error: {e}")
# print(user)

# Working with model attributes
# print(user.name)
# print(user.age)
# print(user.email)

# Example of Default Values
# user2 = UserProfile(name="Tuyen ", email="tuyen@example.com")
# print(user2)

# Example of using field_validator
user3 = UserProfile(name="Tuyen", age=20, email="invalid_email", is_active=True)
print(user3)

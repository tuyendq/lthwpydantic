from pydantic import BaseModel, Field, EmailStr, ValidationError
from pydantic import EmailStr

# Define UserProfile model
class UserProfile(BaseModel):
    name: str
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr  # Using EmailStr for email validation
    is_active: bool = True  # Default value
    # age: int = 18  # Default value
    age: int = Field(ge=18)  # Default value and validation
    
try:
    user_invalid_email = UserProfile(name="Tuyen ", username="tuyen", age=18, email="tuyen@example.com")
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

# Example of using EmailStr for email validation
# user_validate_email = UserProfile(name="Tuyen", age=20, email="invalid_email", is_active=True)
# print(user_validate_email)

# Example of using Field to validate age greater than or equal
user_validate_age = UserProfile(name="John", username="john", age=17, email="john@example.com")
print(user_validate_age)

# user_validate_age_int = UserProfile(name="John", age="17", email="john@example.com")
# print(user_validate_age_int)

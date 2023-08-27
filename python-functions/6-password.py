def validate_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not (has_upper and has_lower and has_digit):
        return False
    
    # Check for spaces
    if ' ' in password:
        return False
    
    return True

import re

def check_password_strength(password):
# Check password length
if len(password) < 8:
return 'Weak'
if len(password) < 12:
strength = 'Medium'
else:
strength = 'Strong'

# Check for mixed case
if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
return 'Weak'

# Check for digits
if not any(c.isdigit() for c in password):
return 'Weak'

# Check for special characters
if not any(not c.isalnum() for c in password):
return 'Weak'

# Check for common passwords
with open('common_passwords.txt') as f:
for line in f:
if password == line.strip():
return 'Weak'

return strength

# Test password strength checker
print(check_password_strength('password'))
print(check_password_strength('P@55w0rd'))
print(check_password_strength('P@55w0rd123!'))
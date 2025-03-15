
class PassUtil:
    @staticmethod
    def testPassStrong(password: str) -> bool:
        #the password should be longer than 10 words
        #the password should contain Upper and lower case
        if len(password) < 10:
            return False
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)

        return has_upper and has_lower
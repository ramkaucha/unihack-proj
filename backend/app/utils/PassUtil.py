import bcrypt
class PassUtil:
    @staticmethod
    def encryptPassword(password: str):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_pw.decode('utf-8')
    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
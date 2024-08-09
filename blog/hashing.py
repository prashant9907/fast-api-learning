from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def hash_with_bcrypt(password):
        return pwd_context.hash(password)
        



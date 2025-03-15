from service.user_service import UserService

#data from frontend: "user_id", "user_name", "password", "email", "is_delete"

class user_controller:
    def register(self, data):
        userName = data.get("user_name") if data else None
        password = data.get("password") if data else None
        email = data.get("email") if data else None
        return UserService.register(userName, password, email)
    
    def login(self, data):
        userName = data.get("user_name") if data else None
        password = data.get("password") if data else None
        return UserService.login(userName, password)
    
    def query_user_by_name(self, data):
        name = data.get("user_name") if data else None
        return UserService.query_user_by_name(name)
    
    def update_user_detail(self, data):
        id = data.get("user_id") if data else None
        userName = data.get("user_name") if data else None
        password = data.get("password") if data else None
        email = data.get("email") if data else None
        return UserService.update_user_detail(id, userName, email, password)
    
    def delete_user(self, data):
        id = data.get("user_id") if data else None
        isDelete = data.get("is_delete") if data else None
        return UserService.delete_user(id, isDelete)
        
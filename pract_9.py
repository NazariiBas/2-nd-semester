class Error:
    def handle_message(self):
        return "Error"

class Success:
    def handle_message(self):
        return "Success"

class Begin:
    pass

class B:
    pass

error_instance = Error()
success_instance = Success()
begin_instance = Begin()
b_instance = B()


if hasattr(begin_instance, 'handle_message'):
    print(begin_instance.handle_message())
else:
    print("No handle_message method for Begin class")

if hasattr(b_instance, 'handle_message'):
    print(b_instance.handle_message())
else:
    print("No handle_message method for B class")

### Decorator

def main_welcome(func):
    
    def sub_welcome_method():
        print("Welcome to the advance python course.")
        func()
        print("Please learn these concepts properly")
    
    return sub_welcome_method()

# def course_introduction():
#     print("This is an advance python course.")

# course_introduction()

# main_welcome(course_introduction)

@main_welcome
def course_introduction():
    print("This is an advanced python course.")

from turtle import down


login = input('Введите Ваш логин :')

def check_login(sum):
    if login=='admin':
        def wrapper_ok(*args, **kwargs):
            r=sum(*args, **kwargs)
            return r
        return wrapper_ok    
    else:
        def wrapper_bad(*args, **kwargs):
            print("Доступ запрещен!")
            return None
        return wrapper_bad 

@check_login
def my_login(lst):
    return sum(lst)

my_login([1,2,3,4])    
   


# def user_input(txt, exception, message):
#     while True:
#         try:
#             return input(txt)
#         except exception:
#             print(message)

def user_input(txt):
    try:
        return input(txt)
    except ValueError:
        print("kkk")
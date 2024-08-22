def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()

# def test_function(x):
#     if x == 1:
#         print('x=1')
#     else:
#         def inner_function():
#             print('Я в области видимости функции test_function')
#     inner_function()
#     return ''
#
#
# a = test_function(1)
# print(a)


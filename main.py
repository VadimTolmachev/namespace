def test_function():
    name = test_function.__name__
    print(name)

    def inner_function():
        nonlocal name
        print(f'Я в области видимости функции {name}')

    inner_function()


test_function()
#inner_function()
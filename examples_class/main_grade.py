from examples_class.prompt_grades_ import First_Class

if __name__ == '__main__':
    result = First_Class('tosin',40)
    print(result.get_name())
    result.set_name('yemi')
    print(result.get_name())
    result.set_age(27)
    print(result.get_name(), result.get_age())

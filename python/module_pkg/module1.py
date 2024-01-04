print('to cehck whether code execute as program or module')

def f1():
    print('f1 __name__ =',__name__)
    if __name__=='__main__':
        print('f1 __name__ =',__name__)
        print('__name__:::')
        print(__name__)
        print('executed as program')
    else:
        print('executed as module from other program')

f1()
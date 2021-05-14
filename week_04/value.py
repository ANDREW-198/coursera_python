

class Value:

    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value * (1-obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission




def test():
    print('big test start')

    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

    new2_account = Account(0.1532)
    new2_account.amount = 123

    print(new2_account.amount)


if __name__ == '__main__':
    test()
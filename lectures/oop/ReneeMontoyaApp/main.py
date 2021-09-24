from controller import Controller

if __name__ == '__main__':
    while True:
        try:
            controller = Controller()
            controller.choise()
        except ValueError:
            print("Please enter valid data")
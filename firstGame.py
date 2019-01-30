class Game:
    def __init__(self):
        print("Welcome In Muhammad Game.....(^_^)")
        print('Choose Your Game From Our Collection')
        print('Press[1] : Play Even Odd Game')
        print('Press[2] : Play Sum Average Game')
        print('Press[3] : Play Mult Table Game')
        self.Choose_Game()

    
    def Choose_Game(self):
        while True:
            user_choose = input('Enter Your Choose: ')

            if user_choose == 'quit':
                break
            try:
                user_choose = int(user_choose)
                if user_choose == 1:
                    self.Even_Odd_Game()
                elif user_choose == 2:
                    self.Sum_Average_Game()
                elif user_choose == 3:
                    self.Mult_Table_Game()
                else:
                    print('Enter Number From The 1,2 or 3')
            except ValueError:
                print('Please Enter A valid Number')
    

    def Even_Odd_Game(self):
        print('Welcome in the even odd game')
        print('Please enter the number.....press \"x\" to exit')
        while True:
            num = input('Enter the number: ')

            if num == 'x':
                print('Closing the game')
                print('thanks....')
                break


            try:
                num = int(num)
                if num % 2 != 0:
                    print('Even Number')
                else:
                    print('Odd Number')


            except ValueError:
                print('please enter a valid number')
            print('------------------------------------')
    

    def Sum_Average_Game(self):
        pass
    

    def Mult_Table_Game(self):
        print("Welcome In Multiplication App")
        start = int(input("Enter the freast number of range:"))
        end = int(input("Enter the last number of range:"))
        for x in range(start,end + 1):
            for y in range(1,13):
                print('|',x , " X ", y, " = ", x * y, '|')
            print('-----------------------')





game1 = Game()
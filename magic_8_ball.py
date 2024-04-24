print('hello')

import random

#Class def 

class Magic8Ball:
    def __init__(self):
        self.responses = {
#dic
            1: "It is certain.",
            2: "It is decidedly so.",
            3: "Without a doubt.",
            4: "Yes - definitely.",
            5: "You may rely on it.",
            6: "As I see it, yes.",
            7: "Most likely.",
            8: "Outlook good.",
            9: "Yes.",
            10: "Signs point to yes.",
            11: "Reply hazy, try again.",
            12: "Ask again later.",
            13: "Better not tell you now.",
            14: "Cannot predict now.",
            15: "Concentrate and ask again.",
            16: "Don't count on it.",
            17: "My reply is no.",
            18: "My sources say no.",
            19: "Outlook not so good.",
            20: "Very doubtful."
        }

    def shake_ball(self):
        return random.choice(list(self.responses.values()))

#if name is main

if __name__ == "__main__":
    magic_ball = Magic8Ball()
    print("Welcome to the Magic 8 Ball!")
    while True:
        input("Ask the Magic 8 Ball a question (press Enter to exit): ")
        print(magic_ball.shake_ball())

# Magic 8 Ball

import os, random, sys

messages = ['It is certain',
'It is decidedly so',
'Yes, definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

while True:
    print('Ask the Magic 8 ball a question or type \'quit\' to exit.')
    question = input()
    if question.lower() == 'quit':
        sys.exit('Thank you for using the Magic 8 ball.')
    else:
        print(messages[random.randint(0, len(messages) -1)])

import pyjokes
from Clear import clearConsole

clearConsole()
#1. get_joke ()
joke1 = pyjokes.get_joke(language='es', category= 'all')  

#display the joke
print(joke1)

joke2 = pyjokes.get_joke(language='es', category= 'neutral')

#display the joke
print(joke2)


#2. get_jokes ()
jokes = pyjokes.get_jokes(language='es', category= 'neutral')

for i in range(5):
    print(i+1,".",jokes[i])

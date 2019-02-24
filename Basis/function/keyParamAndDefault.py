"""
@author: kongwiki
@file:   keyParamAndDefault.py
@time:   19-2-24上午10:09
@contact: kongwiki@163.com
"""

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)


if __name__ == '__main__':
    printName('Olga', 'Puchmajerova', False)
    printName('Olga', 'Puchmajerova', reverse=False)
    printName('Olga', lastName='Puchmajerova', reverse=False)
    printName(lastName='Puchmajerova', firstName=' Olga', reverse=False)
    # printName('Olga', False, lastName='Puchmajerova')

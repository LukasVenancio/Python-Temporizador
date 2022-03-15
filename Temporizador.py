import time, sys, os

def determinarRange(quantidade, unidade):
    segundos = int(0)

    if unidade == 'minutos':
        segundos = quantidade * 60

    elif unidade == 'horas':
        segundos = quantidade * 3600

    elif unidade == 'segundos':
        segundos = quantidade

    contar(segundos)


def contar(range):
    internoRange = range
    print('Tempo total: {}' .format(internoRange))
    i = 0
    while i <= internoRange :
        sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()
        time.sleep(1)
        i += 1

    desligar()

def desligar():
    os.system("shutdown /s /t 1")


determinarRange(20, 'segundos')
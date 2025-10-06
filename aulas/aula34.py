#Generator functions

def Generator(n=0, maximum=10):
    while True:
        yield n # yield siginifica palsa!
        n += 1

        if n > maximum:
            return 'Acabou!'# seria uma expreção de erro um ctrl + c no caso um stop!
        
gen = Generator()

for n in gen: #reproduzindo sem pausar!
    print(n)
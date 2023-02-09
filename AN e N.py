print('AN N')
escolha = str(input('Qual das operações você deseja: ')).upper()
if escolha == 'AN':
    print('Calculo An')
    a1 = int(input('Digite o valor de a1: '))
    n = int(input('Digite o valor de n: '))
    r = int(input('Digite a razão: '))
    n0 = n
    # print('O valor do an é (An = a1 + (n-1).r')
    n1 = n - 1
    print('An=a1+(n-1).r\n'
          'a{}={}+({}-1).{}'.format(n, a1, n, r))
    print('a{}={}+{}.{}'.format(n, a1, n1, r))
    n2 = n1 * r
    print('a{}={}+{}'.format(n, a1, n2))
    n3 = a1 + n2
    print('a{}={}'.format(n, n3))
    print('O valor de a{} é igual a {}: '.format(n0, n3))
else:
    print('Calculo N')
    an = int(input('Digite o an: '))
    a1 = int(input('Digite o valor de a1: '))
    r = int(input('Digite a razão: '))
    n = r
    print('a{}={}+(n-1).{}'.format(an, a1, r))
    n1 = an - a1
    print('a{}={}+{}n-{}'.format(an, a1, r, r))
    print('a{}-{}={}n-{}'.format(an, a1, r, r))
    print(' {}+{}={}n'.format(n1, r, r))
    n2 = n1 + r
    print('{}={}n'.format(n2, r))
    n3 = (n2 / r)
    print('{}n={}'.format(r, n2))
    print('n={}/{}\nn={}'.format(n2, r, n3))
    print('O valor de N é: {}'.format(n3))
#s = senha
def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, muito cruta.'
    
    temNumero = False
    temMaiuscula = False
    simbolo = '!@#$%&'
    temSimbolo = False
    
#c= caracteres
    for c in s:
        if c == ' ':
            return 'Senha inválida, não pode ter espaços'
        if c >= '0' and c <='9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
        if c in simbolo:
            temSimbolo = True
    
    
    if temNumero == False:
        return 'Senha inválida, precisa de um núemro, pelo menos'
    
    if temMaiuscula == False:
        return 'Senha inválida, precisa de uma letra maiscula'
    if not temSimbolo:
        return 'Senha inválida, precisa conter simbolo'
    
#main
senha = input('Digite a senha: ')
r = validarSenha(senha)
print(r)
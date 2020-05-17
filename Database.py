import dbm

#variaveis globais, as duas primeiras para formatação do site, a ultima informará se o site é valido ou não para armazenamento
valores_aceitaveis = ['gov', 'com', 'org', 'edu']
valores_aceitaveis_dois = ['en', 'br']
ok_flag = False

### EXCEÇÕES ###
class TamInvalido(Exception):
    def __str__(self):
        return 'Domínio de tamanho inválido'
    
class SoLetras(Exception):
    def __str__(self):
        return 'Os domínios a serem salvos devem conter apenas letras'

class NotFoundWWW(Exception):
    def __str__(self):
        return 'O domínio deve começar com www'

class DominioInvalido(Exception):
    def __init__(self, dominio):
        self.dominio = dominio
    def __str__(self):
        return 'O dominio deve ser um dos que seguem: %s'%self.dominio

### FUNÇÕES ### 
def menu():
    """
    função do menu inicial
    """
    
    opc = int(input('\n1 - Cadastrar Site\n2 - Procurar Site\n3 - Listar Sites\n0 - Sair\n---> '))
    if 0 <= opc <= 3:
        return opc
    else:
        menu()

def cadastra_site():
    '''
    Cadastra o site se estiver ok a formatação
    '''

    global ok_flag
    
    keyword = input('Palavra-chave do site: ')
    site = input('Site: ')

    SITE = site.split('.')

    if testa_site(SITE):
        ok_flag = True
        return (keyword, site)
    else:
        cadastra_site()

def testa_site(site):
    '''
    testa se a string passada está nos conformes'
    '''
    global valores_aceitaveis
    global valores_aceitaveis_dois

    try:
        if len(site) > 4:
            raise TamInvalido()
    except TamInvalido:
        print(TamInvalido())
        return False
    
    for partes in site:
        try:
            if not partes.isalpha():
                raise SoLetras()
        except SoLetras:
            print(SoLetras())
            return False

    try:
        if site[0] != 'www':
            raise NotFoundWWW()
    except NotFoundWWW:
        print(NotFoundWWW())
        return False


    try:
        if not site[2] in valores_aceitaveis:
            raise DominioInvalido(valores_aceitaveis)
    except DominioInvalido:
        print(DominioInvalido(valores_aceitaveis))
        return False

    if len(site) == 4:
        try:
            if not site[3] in valores_aceitaveis_dois:
                raise DominioInvalido(valores_aceitaveis_dois)
        except DominioInvalido:
            print(DominioInvalido(valores_aceitaveis_dois))
            return False

    #se tudo passar
    return True

def procura_site(site_procurado, DB):
    if site_procurado in str(DB.keys()):
        return DB[site_procurado].decode()
    else:
        return 'Site não encontrado'

def lista_sites(DB):
    for sites in DB:
        print(sites.decode() + ' -> ' + DB[sites].decode())

        
def main():

    global ok_flag
    
    opc = menu()

    if opc == 1:
        DB = dbm.open('sites.db', 'c')
        
        site = cadastra_site()

        if ok_flag:
            DB[site[0]] = site[1]
            ok_flag = False

        DB.close()

    if opc == 2:
        DB = dbm.open('sites.db', 'r')
        site_procurado = input('Palavra-chave do site: ')
        print('-> ' + procura_site(site_procurado, DB))
        DB.close()

    if opc == 3:
        DB = dbm.open('sites.db', 'r')
        lista_sites(DB)
        
    if opc != 0:
        main()


main()

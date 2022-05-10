"""
Decoradores (Decorators)

O que são decorators?

— Decorators são funções;
— Decorators envolvem outras funções e aprimoram os seus comportamentos;
— Decorators também são exemplos de Higher Order Functions;
— Decorator tem uma sintaxe própria, usando @ (Syntact Sugar / Açúcar Sintático)
— Recebem como parâmetro uma função

||——————————————————————————————————————||
||            Function Decorator        ||
||——————————————————————————————————————||

||——————————————————————————————————————||
||             Função Decorada          ||
||——————————————————————————————————————||
|————————————————————————————————————————|

O Decorator vai aprimorar aquilo que já tem

"""


# Decorators como funções (Sintaxe não recomendada / Sem açúcar sintático)
# Aprimorando a função saudacao() com seja_educado()


def seja_educado(funcao):  # Essa função é o Decorator
    """
    A função seja_educado() recebe como parâmetro uma função
    A função interna sendo() irá exibir 2 mensagens, além de exibir a função() que foi passada
    como parâmetro.
    O retorno da função seja_educado() será a função interna sendo()
    """

    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()  # Executando a função vindo como parâmetro
        print("Tenha um ótimo dia!")

    return sendo  # Retornando a função, mas não a execução


def saudacao():
    print("Seja bem vindo ao nosso programa.")


# Testando seja_educado()

teste = seja_educado(saudacao)

teste()

print('\n')


# Testando 2


def raiva():
    print("Eu não gosto de você")


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Açúcar Sintático) — FORMA RECOMENDADA
print('\n')


def seja_educado_mesmo(funcao):  # ISSO É DECORATOR FUNCTION
    def sendo_mesmo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um excelente dia!")

    return sendo_mesmo


@seja_educado_mesmo  # ISSO É UM DECORATOR
def apresentando():
    print("Meu nome é Maria")


# Testando
apresentando()

print('\n')


@seja_educado_mesmo
def dormir():
    print("Quero dormir....")


dormir()

print('\n')

"""
Imagine um site com as seguintes opções:

|------------------------------------------------
| HOME  | SERVIÇOS  | PRODUTOS  | ADMINISTRATIVO |
-------------------------------------------------
http://www.suaempresa.com.br"

# OBS: Não é código funcional é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect("http://www.suaempresa.com.br")
        
def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar serviços'
    
def produtos(request):
    return 'Pode acessar produtos'
    
@checa_login
def admin(request):
    return 'Pode acessar admin'
"""
# OBS: Não confuda Decorator com Decorator Function

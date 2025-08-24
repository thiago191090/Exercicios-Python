def loginUsuario(perfil): #Função com parâmetro, que identifica se a entrada é igual admin. Caso não seja, retorna usuário comum.
    perfil = perfil.lower()
    if perfil == "admin":
        print("Bem vindo, Administrador!")
    else:
        print("Bem vindo, usuário!")

perfil = input("Digite seu perfil de usuário: \n") #Recebe a variável que será parâmetro da função

loginUsuario(perfil) #Chamada da função

import argparse

parametros = argparse.ArgumentParser()
parametros.add_argument("nome_arquivo")
parametros.add_argument("-o")

argumento = parametros.parse_args()

dicionario = {
    '+' : '\ta[i]++;\n', '-' : '\ta[i]--;\n',
    '>' : '\t++i;\n', '<' : '\t--i;\n',
    '.' : '\tprintf("%c", a[i]);\n', ',' : '\ta[i] = getchar();\n\tgetchar();\n',
    '[' : 'while(a[i]) {\n', ']' : '}\n'
}

def inicializar_cmaismais():
    inicio_codigo = ("#include <bits/stdc++.h>\n\n" +
               "using namespace std;\n\n" +
               "int main(){\n" +
               "\nchar a [9000];\n" + 
               "int i = 0;\n")

    return inicio_codigo

def finalizar_cmaismais():
    fim_codigo = "\nreturn 0;\n}" 
    
    return fim_codigo

def escrever_caracteres(source):
    arquivo = source.read()
    codigo_cmaismais = ""

    for caracter in arquivo:
            if caracter in dicionario:
                codigo_cmaismais += dicionario[caracter]

    return codigo_cmaismais

def escrever_arquivo_cmaismais(codigo_cmaismais, arquivo):
    arquivo.write(codigo_cmaismais)

def parser_brainck_to_cmaismais():
    arquivo_brainck = open(argumento.nome_arquivo, 'r')
    arquivo_cmaismais = open(argumento.o, 'w')

    codigo_cmaismais = ""
    codigo_cmaismais += inicializar_cmaismais()
    codigo_cmaismais += escrever_caracteres(arquivo_brainck)
    codigo_cmaismais += finalizar_cmaismais()

    escrever_arquivo_cmaismais(codigo_cmaismais, arquivo_cmaismais)

parser_brainck_to_cmaismais()
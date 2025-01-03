import streamlit as st

# Função para cifrar um caractere
def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave

    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)

    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

# Função para cifrar texto completo
def cifrar_texto(texto, chave):
    minusculas = 'abcdefghijklmnopqrtuvxwyz'
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cifra = ''

    for caractere in texto:
        if caractere in minusculas:
            caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
        elif caractere in maiusculas:
            caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
        else:
            caractere_cifra = caractere
        cifra += caractere_cifra
    return cifra

# Interface Streamlit
st.title("Cifra de Substituição")

# Entrada de texto
texto = st.text_input("Digite o texto que deseja cifrar:", value="novo dia")

# Entrada para chave
chave = st.number_input("Escolha a chave de deslocamento:", value=3, step=1)

# Botão para cifrar
if st.button("Cifrar Texto"):
    texto_cifrado = cifrar_texto(texto, chave)
    st.write(f"Texto Cifrado: **{texto_cifrado}**")
# Escreva o seu código aqui :-)

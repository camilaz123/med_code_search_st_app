import streamlit as st

st.title("Codificação de condições clínicas")

st.markdown("""
## Nós mudamos de endereço!

A ferramenta de codificação continua disponível gratuitamente, mais estável, com melhor acurácia e, agora, numa infraestrutura que conseguimos gerir melhor :)

Nossa empresa chama-se **VIS Healthcare** e estamos trabalhando em soluções para **reduzir o caos da informação na saúde**. 
            
###### [Acesse aqui](https://vishealthcare.com.br/#/code) a ferramenta de codificação.
            
Mostraremos em breve o que mais estamos desenvolvendo :)
            
Até logo!
            
""")

st.markdown(
    """
    <style>
        [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

st.image("logo.jpg")
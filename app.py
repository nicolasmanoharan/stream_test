import streamlit as st

# Cette ligne crée un simple titre pour l'application web
st.title('Application de Bienvenue avec Streamlit')

# Ceci est un widget qui permet à l'utilisateur d'entrer du texte
name = st.text_input('Entrez votre nom', 'Tapez ici...')

# Un bouton que l'utilisateur peut cliquer pour lancer une action.
if st.button('Dis Bonjour'):
    # Ceci affiche un message de bienvenue si l'utilisateur clique sur le bouton
    st.write(f'Bonjour, {name}!')

# Ceci est pour exécuter l'application en utilisant Streamlit.
if __name__ == '__main__':
    st.run()

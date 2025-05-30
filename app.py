import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="ebac",
                   page_icon="data:image/jpeg;base64,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"           
)
st.markdown("""
    <h1 style='
        text-align: center;
        background: linear-gradient(to right, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        color: transparent;
    '>
        Project 2: Exploratory Analysis
    </h1>
""", unsafe_allow_html=True)
sns.set(context='talk', style='ticks')

renda = pd.read_csv('./input/renda_salvo.csv')
renda['posse_de_veiculo'] = renda['posse_de_veiculo'].map({True: 'Yes', False: 'No'})
renda['posse_de_imovel'] = renda['posse_de_imovel'].map({True: 'Yes', False: 'No'})


if st.checkbox('Show database'):
    st.dataframe(renda)

st.markdown('--------------------------------')

fig, ax = plt.subplots(6,1,figsize=(10,70))
st.markdown("""
    <h3 style='text-align: center;'>
        <b>Charts over time: univariate</b>
    </h3>
""", unsafe_allow_html=True)

# Histograma
renda[['log_renda']].plot(kind='hist', bins=50, ax=ax[0], legend=True)
ax[0].set_title("Distribuction in log(Renda)")

# Linha por categorias
sns.barplot(x='tipo_renda', y='log_renda', hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].set_xlabel('')
ax[1].set_ylabel('Log(Renda)')
ax[1].set_title("Log(Renda) for Posse de Imóvel")

sns.barplot(x='tipo_renda', y='log_renda', hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].set_xlabel('')
ax[2].set_ylabel('Log(Renda)')
ax[2].set_title("Log(Renda) for Posse de Veículo")

sns.barplot(x='tipo_renda', y='log_renda', hue='educacao', data=renda, ax=ax[3])
ax[3].set_xlabel('')
ax[3].set_ylabel('Log(Renda)')
ax[3].set_title("Log(Renda) for Educação")

sns.barplot(x='tipo_renda', y='log_renda', hue='estado_civil', data=renda, ax=ax[4])
ax[4].set_xlabel('')
ax[4].set_ylabel('Log(Renda)')
ax[4].set_title("Log(Renda) for Estado civil")

sns.barplot(x='tipo_renda', y='log_renda', hue='tipo_residencia', data=renda, ax=ax[5])
ax[5].set_xlabel('')
ax[5].set_ylabel('Log(Renda)')
ax[5].set_title("Log(Renda) for Tipo de Residência")

# Ajustes visuais
for a in ax[1:]:
    a.tick_params(axis='x', rotation=45)

sns.despine()
plt.tight_layout()
st.pyplot(fig)


st.markdown('--------------------------------')
st.markdown("<h3 style='text-align: center;'>Charts over time: bivariate</h3>", unsafe_allow_html=True)

fig, ax = plt.subplots(7, 1, figsize=(10, 50))

sns.barplot(x='posse_de_imovel', y='log_renda', data=renda, ax=ax[0], palette='Set2')
ax[0].set_xlabel('posse de imovel')
ax[0].set_ylabel('Renda')
ax[0].set_title("Renda for Posse de Imóvel")

sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1], palette='Set2')
ax[1].set_xlabel('posse de veículo')
ax[1].set_ylabel('Renda')
ax[1].set_title("Renda for Posse de Veículo")

sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2], palette='Set2')
ax[2].set_xlabel('Quantidade de filhos')
ax[2].set_ylabel('Renda')
ax[2].set_title("Renda for Quantidade de Filhos")

sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3], palette='Set2')
ax[3].set_xlabel('Tipo de renda')
ax[3].set_ylabel('Renda')
ax[3].set_title("Renda for Tipo de Renda")

sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4], palette='Set2')
ax[4].set_xlabel('Educação')
ax[4].set_ylabel('Renda')
ax[4].set_title("Renda for Escolaridade")

sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5], palette='Set2')
ax[5].set_xlabel('Estado civil')
ax[5].set_ylabel('Renda')
ax[5].set_title("Renda for Estado Civil")

sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6], palette='Set2')
ax[6].set_xlabel('Tipo de residência')
ax[6].set_ylabel('Renda')
ax[6].set_title("Renda for Tipo de Residência")

# Ajustes visuais
for a in ax:
    a.tick_params(axis='x', rotation=45)
    a.set_facecolor("#f9f9f9")  # cor de fundo suave


sns.despine()
plt.tight_layout()
st.pyplot(fig)

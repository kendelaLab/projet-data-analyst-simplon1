import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

df=données.copy()
# Affichage des vraibles
df.info()

# Création du chiffre d'affaires
df["ca"] = df["prix"] * df["qte"]

# a. Les ventes par produit
ventes_par_produit = (
    df.groupby("produit", as_index=False)["qte"].sum().sort_values(by="qte", ascending=False)
)

# b. Le chiffre d'affaires par produit
ca_par_produit = (
    df.groupby("produit", as_index=False)["ca"].sum().sort_values(by="ca", ascending=False)
)

# Affichage console
print("------------------------------------------")
print("*** Ventes par produit ***")
print(ventes_par_produit)
print("------------------------------------------")
print("\n*** Chiffre d'affaires par produit ***")
print(ca_par_produit)

# Graphique 1 : ventes par produit
fig1 = px.bar(
    ventes_par_produit,
    x="produit",
    y="qte",
    title="Ventes par produit",
    labels={"produit": "Produit", "qte": "Quantité vendue"},
)
fig1.write_html("images/ventes_par_produit.html")

# Graphique 2 : chiffre d'affaires par produit
fig2 = px.bar(
    ca_par_produit,
    x="produit",
    y="ca",
    title="Chiffre d'affaires par produit",
    labels={"produit": "Produit", "ca": "Chiffre d'affaires"},
)
fig2.write_html("images/ca_par_produit.html")

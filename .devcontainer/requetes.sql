--Affichage de base ventes
SELECT * FROM ventes;
--a) Chiffre d'affaires total
SELECT SUM (prix * qte) AS chiffre_affaires_total
FROM ventes;

-- b. ventes par produit 
SELECT produit, SUM (qte) As ventes_totales
From ventes 
GROUP by produit
ORder BY ventes_totales DESC;

--c Ventes par régionde
SELECT region, SUM(qte) AS ventes_totales
FROM ventes
GROUP BY region
ORDER BY ventes_totales DESC;
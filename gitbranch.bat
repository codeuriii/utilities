@echo off
:: Demande à l'utilisateur d'entrer l'URL du dépôt distant
set /p repoURL=Entrez l'URL du dépôt distant (upstream) : 

:: Demande le nom de la branche source sur le dépôt upstream
set /p sourceBranch=Entrez le nom de la branche source sur upstream (ex: main) : 

:: Demande à l'utilisateur de nommer la nouvelle branche locale
set /p newBranch=Entrez le nom de votre nouvelle branche locale : 

:: Ajoute le dépôt distant upstream
git remote add upstream %repoURL%
echo Dépôt upstream ajouté : %repoURL%

:: Récupère les mises à jour du dépôt upstream
git fetch upstream
echo Mises à jour récupérées depuis %repoURL%.

:: Crée une nouvelle branche locale basée sur la branche source d'upstream
git checkout -b %newBranch% upstream/%sourceBranch%
echo Nouvelle branche locale créée : %newBranch%

:: Pousse la nouvelle branche vers le dépôt origin
git push origin %newBranch%
echo Nouvelle branche poussée sur origin : %newBranch%.

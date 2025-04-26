# Installateur-de-d-pendances
permet l'installer sans passer part le terminal juste le nom des dépendances ex: cryptography 
au lieu de pip install cryptography

Dans ce code, on retrouve ces trois lignes :

python
Copier
Modifier
# Token GitHub et informations du dépôt
GITHUB_TOKEN = "test"  # Remplace par ton propre token
REPO_OWNER = "Enjukar"  # Remplace par le propriétaire du dépôt (ton nom d'utilisateur ou organisation)
REPO_NAME = "Installateur-de-d-pendances"  # Remplace par le nom de ton dépôt
Explication :

Ces informations sont nécessaires pour que le script puisse interagir automatiquement avec GitHub.

Le GITHUB_TOKEN est une clé d'accès privée qui permet d'authentifier le script auprès de GitHub sans avoir besoin de mot de passe. Il est utilisé pour faire des actions comme créer des issues, envoyer des mises à jour, ou lire/modifier le dépôt.

REPO_OWNER indique qui possède le dépôt (ton compte GitHub ou ton organisation).

REPO_NAME précise le nom du dépôt ciblé.

Pourquoi ?
Cela permet par exemple d’automatiser des tâches comme :

Télécharger des fichiers depuis le dépôt,

Poster des rapports d’erreur dans des issues GitHub,

Mettre à jour des fichiers directement via le script.

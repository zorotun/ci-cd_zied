# TP4 — Chaîne CI/CD avec GitHub Actions (template)

**But**: Mettre en place une chaîne CI/CD pour une application Python (FastAPI) avec GitHub Actions.  
Ce dépôt est un modèle prêt à l'emploi : tests, lint, build Docker, publication sur GHCR et déploiement simulé.

## Badges (remplacez `<USER>` et `<REPO>` par vos valeurs)
![CI](https://github.com/<USER>/<REPO>/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/<USER>/<REPO>/actions/workflows/docker.yml/badge.svg)

## Structure du projet
```
app/
  __init__.py
  main.py
tests/
  test_main.py
requirements.txt
Dockerfile
.github/workflows/ci.yml
.github/workflows/docker.yml
.github/workflows/deploy.yml
```

## Exécution locale rapide
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# dev tools for local test
pip install pytest pytest-cov coverage ruff
pytest --cov=app
```

## Construire et lancer en local
```bash
docker build -t ci-cd-demo .
docker run -p 8000:8000 ci-cd-demo
# puis ouvrir http://localhost:8000
```

## GitHub (basics)
1. Créez un dépôt GitHub (ex: `ci-cd_votre_nom`) et poussez le projet sur `main`.
2. Activez les permissions Actions > Workflow permissions -> **Read and write** (pour permettre au `GITHUB_TOKEN` de publier sur GHCR).
3. Créez l'environnement `production` dans `Settings > Environments` et ajoutez une **environment secret** `APP_SECRET`. Ajoutez aussi un approbateur si vous voulez une validation manuelle.
4. Pour construire et publier l'image Docker : créez un tag `git tag v1.0.0 && git push origin v1.0.0`.

## Remarques
- Le job CI échouera si la couverture est inférieure à 80% (option `--fail-under=80`).
- Le workflow `deploy.yml` est déclenché manuellement (workflow_dispatch) et utilise l'environnement `production` — ce qui provoque une approbation si vous avez configuré des règles d'environnement sur GitHub.

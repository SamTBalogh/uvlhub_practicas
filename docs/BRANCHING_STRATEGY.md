# Branching strategy (no Pull Requests)

## Intent
Se adopta un modelo de ramas predecible para mantener `main` estable, integrar cambios en `develop` y trabajar con ramas de corta duración, reduciendo conflictos y facilitando revertidos.

La integración se realiza mediante merges locales y `git push` directo. No se utiliza flujo de Pull Requests.

## Ramas de larga duración

### main
`main` representa el estado desplegable o de producción.
Se evita el trabajo directo sobre `main`.
Los cambios llegan a `main` desde `develop` (release) o desde `hotfix/*` (urgencias).

### develop
`develop` concentra la integración del trabajo diario.
Las ramas de trabajo se crean desde `develop` y se integran de vuelta en `develop`.

## Ramas de corta duración
Toda tarea se implementa en una rama de corta duración.

Criterios:
- Duración objetivo: 1 a 3 días. Evitar superar 5 días laborales.
- Cambio acotado: una intención por rama.
- Integración frecuente: Actualizar la rama desde su base para minimizar conflictos.
- Limpieza: Eliminar la rama tras integrarla.

## Tipos de ramas y convención de nombres
Formato:

`<type>/<scope>-<short-slug>`

- `<type>`: Tipo de rama (listado abajo).
- `<scope>`: Módulo o área (api, frontend, infra, docs, auth, etc.).
- `<short-slug>`: Descripción breve en kebab-case.

Ejemplos:
- `feature/frontend-card-details`
- `bugfix/api-null-pointer-login`
- `cicd/infra-dependency-check-cache`
- `fix/frontend-navbar-typo`
- `chore/repo-bump-deps`
- `style/frontend-prettier-run`
- `docs/repo-branching-strategy`

### feature/*
Funcionalidad nueva.
Base: `develop`. Destino: `develop`.

### bugfix/*
Corrección de defectos funcionales o de usuario.
Base: `develop`. Destino: `develop`.

### fix/*
Arreglos pequeños y muy acotados.
Base: `develop`. Destino: `develop`.

### cicd/*
Pipelines, workflows, despliegue, infraestructura.
Base: `develop`. Destino: `develop`.

### chore/*
Mantenimiento, dependencias, tooling, refactor sin cambio funcional.
Base: `develop`. Destino: `develop`.

### style/*
Formato, lint, cambios puramente estilísticos.
Base: `develop`. Destino: `develop`.

### docs/*
Documentación.
Base: `develop`. Destino: `develop`.

### hotfix/*
Correcciones urgentes cuando `main` está afectada.
Base: `main`. Destino: `main` y después, sincronización hacia `develop`.

## Integración sin Pull Requests

### Integrar una rama de trabajo en develop
Mrge con commit para dejar rastro explícito de integración.

Comandos:
```bash
git checkout develop
git pull
git merge --no-ff feature/frontend-card-details
git push
git branch -d feature/frontend-card-details
git push origin --delete feature/frontend-card-details

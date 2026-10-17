# FlowBase Web — Application repository

The app code, tests, Dockerfile and build CI live HERE; no Kubernetes manifests or Helm values live here.

- A pull request runs tests and a smoke-test Docker build, but does **not** publish images.
- A merge to `main` runs tests and publishes a multi-architecture image to GHCR tagged `sha-<commit>`.
- Deployment requires an explicit, separately reviewed PR in `flowbase-argocd-demo` updating an image **digest**.
- Current source starts at v1. v2 is introduced by a **subsequent app PR** using the separate upgrade kit.

This is intentionally a dummy storefront, not a payment or real checkout backend.

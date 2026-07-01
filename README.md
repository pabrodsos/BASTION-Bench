# BASTION-Bench

Benchmark bilingue EN/ES para evaluar trade-offs entre seguridad y utilidad en modelos LLM open-weight.

El proyecto distingue dos bloques:

- **Operational Instructions**: tareas tecnicas legitimas, sensibles o dual-use.
- **Normative Instructions**: riesgos de dano, sesgo, desinformacion, discriminacion, privacidad y abuso.

La fuente de planificacion esta fuera de este repo tecnico, en `../knowledge/01_Project/BASTION_Bench_TFG_plan_contexto.md`.

## Planned CLI

```bash
uv run bastion validate-dataset
uv run bastion run --model qwen --condition baseline
uv run bastion score
uv run bastion metrics
uv run bastion compare --models qwen,llama,mistral
uv run bastion report
```

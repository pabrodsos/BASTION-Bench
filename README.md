# BASTION-Bench

BASTION-Bench is a bilingual EN/ES benchmark for evaluating safety-utility trade-offs in open-weight LLMs.

The project is organized around two benchmark blocks:

- **Operational Instructions**: legitimate, sensitive, or dual-use technical tasks.
- **Normative Instructions**: risks involving harm, misinformation, bias, discrimination, privacy, and abuse.

The research planning notes live outside this technical repository.

## Planned CLI

```bash
uv run bastion validate-dataset
uv run bastion run --model qwen --condition baseline
uv run bastion score
uv run bastion metrics
uv run bastion compare --models qwen,llama,mistral
uv run bastion report
```

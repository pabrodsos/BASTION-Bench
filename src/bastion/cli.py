import typer

app = typer.Typer(help="BASTION-Bench evaluation CLI.")


@app.command()
def validate_dataset(path: str = "data/prompts/bastion_v0.jsonl") -> None:
    """Validate a BASTION prompt dataset."""
    typer.echo(f"Dataset validation is not implemented yet: {path}")


@app.command()
def run(model: str, condition: str = "baseline") -> None:
    """Run a model on BASTION-Bench."""
    typer.echo(f"Model run is not implemented yet: model={model}, condition={condition}")


@app.command()
def score(responses: str = "data/responses/responses.jsonl") -> None:
    """Score model responses."""
    typer.echo(f"Scoring is not implemented yet: {responses}")


@app.command()
def metrics(scores: str = "data/scores/scores.jsonl") -> None:
    """Compute benchmark metrics."""
    typer.echo(f"Metrics are not implemented yet: {scores}")


@app.command()
def compare(models: str) -> None:
    """Compare multiple model runs."""
    typer.echo(f"Comparison is not implemented yet: {models}")


@app.command()
def report() -> None:
    """Generate report tables and figures."""
    typer.echo("Report generation is not implemented yet")

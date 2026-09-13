import typer
app=typer.Typer()
@app.command()
def main(name:int):
    print(name+name)

if __name__ == "__main__":
    app()
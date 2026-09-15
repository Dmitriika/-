import typer
app=typer.Typer()
@app.command()
def main(number1:int,operation:str,number2:int):
    if operation=='+':
        print(float(number1) + float(number2))
    elif operation=='-':
        print(float(number1) - float(number2))
    elif operation in ('*','x'):
        print(float(number1) * float(number2))
    elif operation=='/':
        print(float(number1) / float(number2))
if __name__ == "__main__":
    app()

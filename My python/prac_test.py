from pathlib import Path
import json
path=Path('prac.json')
def ask(path):
    content=path.read_text()
    l=json.loads(content)
    if path.exists():
        print(f"you have saved this data : \n {l}")
        print(f"do you wanna rewrite:")
        print("Wanna recreate file :")
        yes_no=input(" 'yes' or 'no' : ")
        if yes_no=='yes':
            ln=int(input("Enter your data : "))
            data=json.dumps(ln)
            content=path.write_text(data)
        else:
            print(f"Have a good day !")
    else:
        print("No such file found !")
        print("Wanna create a new file : 'yes' or 'no'")
        yes_no=input(" 'yes' or 'no' : ")
        if yes_no=='yes':
            ln=int(input("Enter your data : "))
            data=json.dumps(ln)
            content=path.write_text(data)
        else:
            print(f"Have a good day !")    
ask(path)

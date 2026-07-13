from pathlib import Path
import os
'''
aa=str(Path("spam","bacon","eggs"))
print(aa)
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\AI',filename))
print(Path('spam') / 'bacon' / 'eggs')  #

#os.chdir("N:\AI\phase-1-python\week-6")
print(Path.cwd())
print(Path.home())

#os.makedirs("N:\Testfolder\walnut\waffles")
#Path(r"N:\old_test\abc\def\tre").mkdir()
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())
print(os.path.abspath("."))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))
print(os.path.relpath("N:\AI\phase-1-python\week-6","N:\AI"))

p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.drive)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.exists())
print(Path.cwd())
print(Path.cwd().parents)
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])

calcFilePath = "C:/Users/Al/spam.txt"
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))
print('/usr/bin'.split(os. sep))'''

print(os.path.getsize("N:\AI\phase-1-python"))
#print(os.listdir("N:\AI\phase-1-python\week-6\day-40"))

p=Path.cwd()
#print(list(p.glob("practice?.py")))

p=open(Path.cwd()/"hello.txt","r")
#p.write_text("hello world")
#p.read_text()
#content=p.readlines()
#print(content)
# writes overwrites
file=open(Path.cwd()/"demo.txt","a")
#content1=file.write("hello, this is demo file.\njust learning to open file.\n")
#content2=file.write("damn to know about append.")
file.close()
file=open(Path.cwd()/"demo.txt")
content=file.read()
print(content)
file.close()

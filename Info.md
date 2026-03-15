[!NOTE]
os.rename(```old, new```)
Does Not Raise An Exception Even If The File We Are Changing The Name Exists in parameter 'new'
[!TIP]
For This Purpose Use Conditional Statement Along With pathlib Module :
if ```pathlib.Path(path).exists():
    raise Exception
```

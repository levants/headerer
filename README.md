## Header
Document and paper header modifier for file name to save
```bash
sh text_modify.sh "Your Text goes: Here"
```
or
```bash
sh text_modify.sh Your Text goes: Here
```
copies to the clipboard:
```bash
your_text_goes_here
```

## PDF File Name Generator

Generates PDF file name from header

```bash
sh text_modify.sh "Your Text goes: Here" --pdf
```
or
```bash
sh text_modify.sh Your Text goes: Here --pdf
```
copies to the clipboard:
```bash
your_text_goes_here
your_text_goes_here.pdf
```
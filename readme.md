# Tutorial de PyInstaller com tesseract e poppler

## Instale as dependências:
```
pip install -r requirements.txt
```

## Testar o programa:
```
python main.py
```

## Buildar com linha de comando:
```
pyinstaller --onefile --add-binary "C:/vcpkg/installed/x64-windows-static/tools/tesseract/tesseract.exe;." --add-binary "C:/poppler/Library/bin;poppler/bin" --add-data "C:/vcpkg/installed/x64-windows-static/share/tessdata;tessdata" --add-data "app;app" --name main --noconsole main.py
```

## Buildar com o spec:
```
pyinstaller main.spec
```

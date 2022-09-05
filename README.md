# dialog_magyarito

Program angol nyelvű e-könyvek dialógusformátumának az átalakítására magyar formátumra. 

Az angol formátum ""-ök közé teszi a dialógusokat, a magyar regényformátum pedig gondolatjeleket használ, erre cseréli ki őket.

Jelenleg csak epub formátummal működik és “” (U+201C / U+201D) unicode karakterekre.

Használni vagy a magyarito.py letöltésével és terminálban való futtatásával lehet (ehhez viszont lehet, hogy telepíteni kell a függőségeket is.)

Python 3.10.-ben íródott a következő csomagok felhasználásával:
    - Tkinter
    - zipfile
    - os
    - pathlib
    - shutil

Készítettem belőle egy .exe fájlt is, ez szintén letölthető a repóból, ezesetben sima dupla kattal indítható.

A program meg fog jeleníteni egy felugró ablakot, ahol ki kell választani az átalakítandó epub fájlt, majd egy második felugró ablakban a célmappát, ahová el fogja készíteni az átalakított epub fájlt. 

Jelenleg a program csak egy fájl átalakítását támogatja egyszerre.
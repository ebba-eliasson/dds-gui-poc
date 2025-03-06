# DDS GUI POC

## Goal

1. Investigate the use of PyQt6 and Textualize to create a GUI for the DDS.
2. Create a mock up of a GUI using the chosen library.

### Main Criterias for the GUI Framework/Library

- Easy to understand and use 
- Easy to maintain 
- Good documentation and community support

## GUI Framework/Library

### Choosing the GUI Framework/Library

During discussions the following libraries were considered:

- PyQt6
- Textualize
- Other python based GUI frameworks (tkinter, kivy, pyside6, etc.)
- Web development frameworks (Electron, Tauri, etc.)

Pros and cons between the different python based GUI/TUI frameworks are derived from the following articles:

- [Python GUI : Difference between tkinter, PyQt, and Kivy](https://medium.com/@qasim.coder/python-gui-smackdown-unleashing-the-power-of-tkinter-pyqt-and-kivy-e7b05d0e862)
- [PyQt vs. Tkinter — Which Should You Choose for Your Next GUI Project?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/)
- [Best Python GUI Libraries](https://www.bairesdev.com/blog/best-python-gui-libraries/)
- [PyQt5 vs PySide2](https://www.pythonguis.com/faq/pyqt5-vs-pyside2/)
- [Desktop App Development - PyQt vs Tkinter vs Electron](https://apfirebolt.hashnode.dev/desktop-app-development-pyqt-vs-tkinter-vs-electron)


| Library | Best For | Pros | Cons | Licencing |
|---------|------|------|------|------|
| PyQt6 | Desktop applications, multimedia, scientific, and engineering applications | Feature rich, extensive documentation, active community support | Larger and  more complex, supposedly a steeper learning curve | GPL   
| Textualize | CLI integration | Can be served as an web application, low requirments | Might still feel like a CLI application for end users | MIT
| tkinter | Simple GUIs, small portable applications | Simple and standardized, already included in python | Limited UI, looks outdated out of the box, needs multiple dependencies to look modern, lacks more complex features | Python
| kivy | Mulit platform applications (both mobile and desktop) | Support for touch and gesture interfaces| Smaller community, less mature, less documentation | MIT
| pyside6 | Same as PyQt6 | Same as PyQt6 | Same as PyQt6 | LGPL
| Electron | Desktop applications | Uses modern web technologies (HTML, CSS, JavaScript), good documentation, good community support | Not a python library, heavy application | MIT
|Tauri | Desktop applications | Smaller app size than Electron | Less mature than Electron | MIT

Going forward with PyQt6, Textualize and ??.

## Prototype 

Design file used to test the libraries:

![Image](./assets/App.png)

## PyQt6

### Installation

```bash
pip install PyQt6
``` 

### Running the application

```bash
python pyqt/app.py
```

### Comments
- Documentation for PyQt6 was generally hard to navigate and understand.
- Using the widgets was relatively straight forward.
- The styling was a bit more difficult to understand.

## Textualize

### Installation

```bash
pip install textual
```

### Running the application

```bash
textual run pyqt/app.py
```


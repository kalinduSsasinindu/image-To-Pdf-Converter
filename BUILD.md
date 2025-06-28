# Building Executable Files

This guide explains how to build standalone executable files from the source code.

## Overview

The project uses [PyInstaller](https://pyinstaller.readthedocs.io/) to create standalone executable files that can run on Windows systems without requiring Python to be installed.

## Prerequisites

### Required Software

- **Python 3.6+** (tested with Python 3.12 and 3.13)
- **pip** (Python package installer)
- **Git** (for version control)

### Required Python Packages

```bash
pip install -r requirements.txt
pip install pyinstaller
```

### Manual Package Installation

If you prefer to install packages manually:

```bash
pip install Pillow reportlab pyinstaller
```

## Build Process

### 1. Prepare the Environment

```bash
# Clone the repository
git clone https://github.com/kalinduSsasinindu/image-To-Pdf-Converter.git
cd image-To-Pdf-Converter

# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Test that everything works
python test_converter.py
```

### 2. Build GUI Executable

```bash
# Build the GUI version (no console window)
python -m PyInstaller --onefile --windowed --name "Image2PDF_GUI" gui_converter.py
```

**Options explained:**
- `--onefile`: Creates a single executable file
- `--windowed`: No console window (GUI only)
- `--name`: Name of the output executable

### 3. Build CLI Executable

```bash
# Build the command-line version (with console)
python -m PyInstaller --onefile --console --name "Image2PDF_CLI" image_to_pdf_converter.py
```

**Options explained:**
- `--onefile`: Creates a single executable file
- `--console`: Keeps console window for CLI interaction
- `--name`: Name of the output executable

### 4. Locate Built Files

After building, the executable files will be in the `dist/` directory:

```
dist/
├── Image2PDF_GUI.exe    # GUI version (~26 MB)
└── Image2PDF_CLI.exe    # CLI version (~23 MB)
```

## Advanced Build Options

### Custom Build Script

You can create a batch file for easier building:

**`build.bat`:**
```batch
@echo off
echo Building Image2PDF Converter executables...

echo.
echo Building GUI version...
python -m PyInstaller --onefile --windowed --name "Image2PDF_GUI" gui_converter.py

echo.
echo Building CLI version...
python -m PyInstaller --onefile --console --name "Image2PDF_CLI" image_to_pdf_converter.py

echo.
echo Build complete! Check the dist/ folder for executables.
pause
```

### PyInstaller Spec Files

For more control, you can use spec files:

**`gui_build.spec`:**
```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['gui_converter.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.ttk',
        'reportlab.pdfgen.canvas',
        'reportlab.lib.pagesizes',
        'reportlab.lib.utils',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Image2PDF_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
```

Build using spec file:
```bash
python -m PyInstaller gui_build.spec
```

## Build Optimization

### Reducing File Size

1. **Exclude unnecessary modules:**
   ```bash
   python -m PyInstaller --onefile --exclude-module matplotlib --exclude-module numpy gui_converter.py
   ```

2. **Use UPX compression** (if available):
   ```bash
   python -m PyInstaller --onefile --upx-dir=/path/to/upx gui_converter.py
   ```

### Including Additional Files

If you need to include additional files (icons, data files):

```python
# In spec file
datas=[
    ('icon.ico', '.'),
    ('data/*', 'data'),
],
```

## Testing Built Executables

### Basic Testing

```bash
# Test CLI version
dist\Image2PDF_CLI.exe --help

# Test GUI version (double-click or from command line)
dist\Image2PDF_GUI.exe
```

### Comprehensive Testing

1. **Test all features:**
   - Single image conversion
   - Multiple image conversion
   - Directory batch processing
   - Different image formats
   - Custom page sizes and margins

2. **Test on clean systems:**
   - Test on computers without Python installed
   - Test on different Windows versions
   - Test with different user permission levels

3. **Performance testing:**
   - Large image files
   - Many images at once
   - Long file paths
   - Special characters in file names

## Troubleshooting

### Common Build Issues

**1. "Module not found" errors:**
```bash
# Add missing modules to hiddenimports in spec file
hiddenimports=['missing_module_name']
```

**2. "Permission denied" during build:**
```bash
# Run command prompt as administrator
# Or exclude antivirus from scanning the build directory
```

**3. Large executable size:**
```bash
# Use --exclude-module to remove unused packages
python -m PyInstaller --onefile --exclude-module numpy --exclude-module matplotlib gui_converter.py
```

**4. Runtime errors in built executable:**
```bash
# Build with --debug for more information
python -m PyInstaller --onefile --debug=all gui_converter.py
```

### Build Environment Issues

**Python Path Issues:**
```bash
# Use full Python path if needed
C:\Path\To\Python\python.exe -m PyInstaller --onefile gui_converter.py
```

**Missing Dependencies:**
```bash
# Verify all packages are installed
pip list | grep -E "(Pillow|reportlab|pyinstaller)"
```

### Runtime Issues

**1. "Failed to execute script" error:**
- Usually caused by missing dependencies
- Build with `--debug=all` to see detailed error messages
- Check that all imports work in the source code

**2. GUI doesn't start:**
- Ensure `--windowed` flag was used for GUI build
- Test GUI source code first: `python gui_converter.py`
- Check for tkinter availability

**3. File access errors:**
- Ensure executable has proper permissions
- Test in different directories
- Check antivirus isn't blocking the executable

## Distribution

### Preparing for Distribution

1. **Test extensively** on multiple systems
2. **Create checksums** for verification:
   ```bash
   certutil -hashfile Image2PDF_GUI.exe SHA256
   certutil -hashfile Image2PDF_CLI.exe SHA256
   ```

3. **Package with documentation:**
   ```
   distribution/
   ├── Image2PDF_GUI.exe
   ├── Image2PDF_CLI.exe
   ├── README.txt
   └── EXECUTABLE_GUIDE.pdf
   ```

### GitHub Releases

To create a release on GitHub:

1. Tag the version: `git tag v1.0.0`
2. Push the tag: `git push origin v1.0.0`
3. Create release on GitHub
4. Upload executable files as release assets

## Version Information

### Adding Version Info to Executables

Create a `version.rc` file for Windows version information:

```rc
1 VERSIONINFO
FILEVERSION 1,0,0,0
PRODUCTVERSION 1,0,0,0
FILEOS 0x40004
FILETYPE 0x1
{
BLOCK "StringFileInfo"
{
    BLOCK "040904B0"
    {
        VALUE "CompanyName", "Image2PDF Converter"
        VALUE "FileDescription", "Convert images to PDF format"
        VALUE "FileVersion", "1.0.0.0"
        VALUE "ProductName", "Image2PDF Converter"
        VALUE "ProductVersion", "1.0.0.0"
    }
}
}
```

## Automation

### GitHub Actions Build

Create `.github/workflows/build.yml` for automated builds:

```yaml
name: Build Executables

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pyinstaller
    - name: Build executables
      run: |
        python -m PyInstaller --onefile --windowed --name "Image2PDF_GUI" gui_converter.py
        python -m PyInstaller --onefile --console --name "Image2PDF_CLI" image_to_pdf_converter.py
    - name: Upload artifacts
      uses: actions/upload-artifact@v2
      with:
        name: executables
        path: dist/*.exe
```

This automated build will create executables whenever you push a new tag to GitHub. 
# Image to PDF Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/image2pdfconverter)
[![PyInstaller](https://img.shields.io/badge/PyInstaller-Supported-green.svg)](https://pyinstaller.readthedocs.io/)

A comprehensive Python application for converting images to PDF format. This tool supports both command-line interface and graphical user interface (GUI) for easy image to PDF conversion.

> 🚀 **Ready-to-use executables available!** No Python installation required for Windows users.

## Table of Contents

- [Quick Start](#quick-start-no-installation-required)
- [Features](#features)
- [Installation from Source](#option-2-install-from-source)
- [Usage](#usage)
- [Examples](#examples)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Documentation](#documentation)

## Features

- **Multiple image formats supported**: JPEG, PNG, BMP, TIFF, GIF, WebP
- **Command-line interface** with various options
- **Graphical user interface** for easy drag-and-drop usage
- **Single image conversion** - Convert one image to one PDF
- **Batch conversion** - Convert multiple images to separate PDFs
- **Multi-page PDF** - Combine multiple images into a single PDF
- **Customizable page sizes** - A4 or Letter format
- **Adjustable margins** - Control PDF layout
- **Automatic image scaling** - Maintains aspect ratio while fitting to page
- **Directory processing** - Convert all images in a folder

## Quick Start (No Installation Required)

### Option 1: Use Executable Files (Recommended)

For users who just want to convert images to PDF without installing Python:

1. **Go to [Releases](https://github.com/yourusername/image2pdfconverter/releases)** 
2. **Download the latest release** containing:
   - `Image2PDF_GUI.exe` - Graphical interface (26MB)
   - `Image2PDF_CLI.exe` - Command-line tool (23MB)
3. **Run the executables** directly - no installation needed!

**See [EXECUTABLE_GUIDE.md](EXECUTABLE_GUIDE.md) for detailed instructions.**

> 💡 **Note**: Executable files are distributed through GitHub Releases, not in the repository itself, to keep the repository lightweight.

### Option 2: Install from Source

If you want to modify the code or use Python directly:

### 2. Install Dependencies

```bash
# Install required packages
pip install Pillow reportlab
```

Or install manually:
```bash
pip install -r requirements.txt
```

### 3. Quick Setup Test

```bash
# Test the installation
python test_converter.py
```

**Note**: If you encounter import errors, you may need to use the full Python path. On Windows, this might be:
```cmd
C:\Users\[username]\AppData\Local\Programs\Python\Python3[version]\python.exe -m pip install Pillow reportlab
```

## Usage

### Command Line Interface

#### Basic Usage

```bash
# Convert single image
python image_to_pdf_converter.py image.jpg

# Convert with custom output name
python image_to_pdf_converter.py image.jpg -o my_document.pdf

# Convert multiple images to separate PDFs
python image_to_pdf_converter.py img1.jpg img2.png img3.bmp
```

**Windows users**: You can use the convenience batch file:
```cmd
# Use the batch file for easier execution
.\convert.bat image_to_pdf_converter.py image.jpg
.\convert.bat gui_converter.py
.\convert.bat test_converter.py
```

#### Advanced Usage

```bash
# Merge multiple images into single PDF
python image_to_pdf_converter.py img1.jpg img2.png -m -o combined.pdf

# Convert all images in a directory
python image_to_pdf_converter.py -d /path/to/images/

# Merge all images in directory into single PDF
python image_to_pdf_converter.py -d /path/to/images/ --merge-all all_images.pdf

# Custom page size and margins
python image_to_pdf_converter.py image.jpg --page-size Letter --margin 72
```

#### Command Line Options

- `images`: Image file(s) to convert
- `-d, --directory`: Directory containing images to convert
- `-o, --output`: Output PDF file path
- `-m, --merge`: Merge multiple images into a single PDF
- `--merge-all`: Merge all images in directory into single PDF
- `--page-size`: PDF page size (A4 or Letter, default: A4)
- `--margin`: Page margin in points (default: 50)

### Graphical User Interface

Launch the GUI application:

```bash
python gui_converter.py
```

#### GUI Features:

1. **Add Images**: Select individual image files
2. **Add Directory**: Add all images from a folder
3. **Clear All**: Remove all selected images
4. **Options**:
   - Page size (A4 or Letter)
   - Margin settings
   - Conversion mode (Separate PDFs or Single PDF)
5. **Output**: Choose output location
6. **Convert**: Start the conversion process

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- GIF (.gif)
- WebP (.webp)

## Examples

### Example 1: Convert Single Image
```bash
python image_to_pdf_converter.py photo.jpg
# Creates: photo.pdf
```

### Example 2: Batch Convert Directory
```bash
python image_to_pdf_converter.py -d ./images/
# Converts all images in ./images/ to separate PDFs
```

### Example 3: Create Multi-page PDF
```bash
python image_to_pdf_converter.py page1.jpg page2.jpg page3.jpg -m -o document.pdf
# Creates: document.pdf with 3 pages
```

### Example 4: Custom Settings
```bash
python image_to_pdf_converter.py image.png --page-size Letter --margin 100 -o custom.pdf
# Creates: custom.pdf with Letter size and larger margins
```

## File Structure

```
image2pdfconverter/
├── .github/workflows/        # GitHub Actions for CI/CD
├── image_to_pdf_converter.py # Main command-line script
├── gui_converter.py          # GUI application
├── test_converter.py         # Test script to verify installation
├── convert.bat              # Windows convenience batch file
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore patterns
├── LICENSE                 # MIT License
├── README.md              # This file
├── EXECUTABLE_GUIDE.md    # Guide for using .exe files
├── CONTRIBUTING.md        # Contributing guidelines
├── BUILD.md              # Build instructions
├── CHANGELOG.md          # Version history
└── venv/                 # Virtual environment (optional)

# Executable files are available in GitHub Releases:
# → Image2PDF_GUI.exe    (GUI executable - 26MB)
# → Image2PDF_CLI.exe    (CLI executable - 23MB)
```

## Troubleshooting

### Common Issues

1. **ImportError for PIL or reportlab**
   ```
   Solution: Install dependencies with: pip install Pillow reportlab
   ```

2. **"No module named 'tkinter'" (Linux/macOS)**
   ```
   Solution: Install tkinter
   # Ubuntu/Debian: sudo apt-get install python3-tk
   # macOS: tkinter is usually included with Python
   ```

3. **Permission denied errors**
   ```
   Solution: Check file permissions and run with appropriate privileges
   ```

4. **Large images causing memory issues**
   ```
   Solution: The script automatically scales images to fit the page size
   ```

### Virtual Environment Issues

If you have trouble with the virtual environment:

1. **On Windows PowerShell**, you might need to enable script execution:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **Alternative activation methods**:
   ```bash
   # Windows Command Prompt
   venv\Scripts\activate.bat
   
   # Windows PowerShell
   venv\Scripts\Activate.ps1
   
   # macOS/Linux
   source venv/bin/activate
   ```

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library for image processing
- ReportLab library for PDF generation
- tkinter for GUI (usually included with Python)

## Contributing

We welcome contributions from the community! Here's how you can help:

- 🐛 **Report Bugs**: Create an issue describing the problem
- 💡 **Suggest Features**: Share your ideas for improvements  
- 🔧 **Submit Code**: Fork the repo and create a pull request
- 📚 **Improve Docs**: Help make our documentation better

Please read our [Contributing Guidelines](CONTRIBUTING.md) for detailed information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Documentation

### 📖 Available Guides

- **[Executable Guide](EXECUTABLE_GUIDE.md)** - How to use the standalone .exe files
- **[Build Guide](BUILD.md)** - How to build executables from source
- **[Contributing](CONTRIBUTING.md)** - Guidelines for contributors
- **[Changelog](CHANGELOG.md)** - Version history and changes

### 🆘 Support

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search [existing issues](https://github.com/yourusername/image2pdfconverter/issues)
3. Create a [new issue](https://github.com/yourusername/image2pdfconverter/issues/new) with details

### 🌟 Show Your Support

If this project helped you, please consider:
- ⭐ **Starring** the repository
- 🐛 **Reporting** any bugs you find
- 💡 **Suggesting** new features
- 🔄 **Sharing** with others who might find it useful

---

**Made with ❤️ for the open source community** 
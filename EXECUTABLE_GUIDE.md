# Image to PDF Converter - Executable Guide

## Overview

This guide covers how to use the standalone executable files that don't require Python to be installed.

## Available Executables

Located in the `dist` folder:

- **`Image2PDF_GUI.exe`** - Graphical User Interface (Recommended for most users)
- **`Image2PDF_CLI.exe`** - Command Line Interface (For advanced users and automation)

## GUI Version (Image2PDF_GUI.exe)

### How to Use

1. **Double-click** `Image2PDF_GUI.exe` to launch the application
2. **Add Images**: Click "Add Images" to select individual files or "Add Directory" to add all images from a folder
3. **Configure Options**:
   - **Page Size**: Choose A4 or Letter
   - **Margin**: Adjust page margins (default: 50 points)
   - **Mode**: Choose "Separate PDFs" or "Single PDF"
4. **Set Output**: Choose where to save the PDF files
5. **Convert**: Click "Convert to PDF" to start the process

### Features

- ✅ Drag and drop interface
- ✅ Progress bar with status updates
- ✅ Support for multiple image formats (JPEG, PNG, BMP, TIFF, GIF, WebP)
- ✅ Batch processing of entire directories
- ✅ Multi-page PDF creation
- ✅ Customizable page sizes and margins

### Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- GIF (.gif)
- WebP (.webp)

## Command Line Version (Image2PDF_CLI.exe)

### Basic Usage

Open Command Prompt or PowerShell in the folder containing the executable and use:

```cmd
# Convert single image
.\Image2PDF_CLI.exe image.jpg

# Convert with custom output name
.\Image2PDF_CLI.exe image.jpg -o my_document.pdf

# Convert multiple images to separate PDFs
.\Image2PDF_CLI.exe img1.jpg img2.png img3.bmp
```

### Advanced Usage

```cmd
# Merge multiple images into single PDF
.\Image2PDF_CLI.exe img1.jpg img2.png -m -o combined.pdf

# Convert all images in a directory
.\Image2PDF_CLI.exe -d "C:\path\to\images\"

# Merge all images in directory into single PDF
.\Image2PDF_CLI.exe -d "C:\path\to\images\" --merge-all all_images.pdf

# Custom page size and margins
.\Image2PDF_CLI.exe image.jpg --page-size Letter --margin 72
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `images` | Image file(s) to convert |
| `-d, --directory` | Directory containing images to convert |
| `-o, --output` | Output PDF file path |
| `-m, --merge` | Merge multiple images into a single PDF |
| `--merge-all` | Merge all images in directory into single PDF |
| `--page-size` | PDF page size (A4 or Letter, default: A4) |
| `--margin` | Page margin in points (default: 50) |

### Help

Get help anytime with:
```cmd
.\Image2PDF_CLI.exe --help
```

## Distribution

### Sharing the Executables

You can share these executable files with others without them needing to install Python or any dependencies:

1. **Copy the `dist` folder** to any Windows computer
2. **Run the executables** directly from the folder
3. **No installation required** - they are completely standalone

### File Sizes

- `Image2PDF_GUI.exe`: ~26 MB
- `Image2PDF_CLI.exe`: ~23 MB

These files include all necessary libraries and dependencies.

## Examples

### Example 1: Convert Photos from Phone

1. Copy photos from your phone to a folder
2. Run `Image2PDF_GUI.exe`
3. Click "Add Directory" and select the folder
4. Choose "Single PDF" mode
5. Set output location
6. Click "Convert to PDF"

### Example 2: Batch Process Documents

```cmd
# Convert all images in Documents folder to separate PDFs
.\Image2PDF_CLI.exe -d "C:\Users\YourName\Documents\ScannedDocs\"

# Merge all receipts into one PDF
.\Image2PDF_CLI.exe -d "C:\Users\YourName\Documents\Receipts\" --merge-all "All_Receipts.pdf"
```

### Example 3: Custom Settings

```cmd
# Create Letter-sized PDF with larger margins
.\Image2PDF_CLI.exe document.jpg --page-size Letter --margin 100 -o "Document_Letter.pdf"
```

## Troubleshooting

### Common Issues

1. **"Windows protected your PC" message**
   - Click "More info" then "Run anyway"
   - This is normal for unsigned executables

2. **File not found errors**
   - Make sure image file paths are correct
   - Use quotes around paths with spaces

3. **Permission denied**
   - Run as administrator if needed
   - Check that output directory is writable

4. **Out of memory errors**
   - Process fewer images at once for very large files
   - Close other applications to free up memory

### Performance Tips

- For best performance, process images in smaller batches
- The GUI version shows progress, making it easier for large jobs
- Both versions automatically scale images to fit the page

## Technical Notes

- Built with PyInstaller
- Includes all Python dependencies
- Compatible with Windows 10/11
- No external dependencies required
- Antivirus software may flag as unknown (false positive)

## Support

If you encounter issues:
1. Check this guide
2. Try the alternative executable (GUI vs CLI)
3. Ensure images are in supported formats
4. Check file permissions and paths 
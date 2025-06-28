# Contributing to Image2PDF Converter

Thank you for your interest in contributing to the Image2PDF Converter project! We welcome contributions from the community.

## Ways to Contribute

- 🐛 **Bug Reports**: Report bugs or issues you encounter
- 💡 **Feature Requests**: Suggest new features or improvements
- 🔧 **Code Contributions**: Submit bug fixes or new features
- 📚 **Documentation**: Improve documentation, examples, or guides
- 🧪 **Testing**: Help test the application on different systems

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/image-To-Pdf-Converter.git
   cd image-To-Pdf-Converter
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run tests** to ensure everything works:
   ```bash
   python test_converter.py
   ```

### Making Changes

1. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly:
   ```bash
   python test_converter.py
   ```
4. **Test both GUI and CLI** interfaces
5. **Commit your changes**:
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```

## Code Style Guidelines

### Python Code Standards

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and reasonably small
- Use type hints where appropriate

### Example Code Style

```python
def convert_image_to_pdf(image_path: str, output_path: str = None) -> str:
    """
    Convert a single image to PDF format.
    
    Args:
        image_path (str): Path to the input image file
        output_path (str, optional): Path for output PDF. Defaults to None.
        
    Returns:
        str: Path to the created PDF file
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If image format is not supported
    """
    # Implementation here
    pass
```

### Commit Message Format

Use clear, descriptive commit messages:

- `Add: New feature description`
- `Fix: Bug fix description`
- `Update: Improvement description`
- `Docs: Documentation changes`
- `Test: Testing changes`

## Testing

### Before Submitting

1. **Run the test suite**:
   ```bash
   python test_converter.py
   ```

2. **Test both interfaces**:
   ```bash
   # CLI interface
   python image_to_pdf_converter.py --help
   
   # GUI interface
   python gui_converter.py
   ```

3. **Test with various image formats**:
   - JPEG, PNG, BMP, TIFF, GIF, WebP
   - Different image sizes
   - Batch operations

4. **Test executable building** (if modifying core functionality):
   ```bash
   python -m PyInstaller --onefile --windowed gui_converter.py
   python -m PyInstaller --onefile --console image_to_pdf_converter.py
   ```

### Test Cases to Consider

- Single image conversion
- Multiple image conversion
- Directory batch processing
- Different page sizes (A4, Letter)
- Various margin settings
- Error handling (invalid files, permissions, etc.)
- Large image files
- Special characters in file paths

## Documentation

### When to Update Documentation

- Adding new features
- Changing existing functionality
- Fixing bugs that affect usage
- Adding new command-line options
- Modifying the GUI interface

### Documentation Files

- `README.md` - Main project documentation
- `EXECUTABLE_GUIDE.md` - Guide for executable usage
- Code comments and docstrings
- Help text in the applications

## Submitting Pull Requests

### Pull Request Process

1. **Ensure your code follows** the style guidelines
2. **Update documentation** if needed
3. **Add or update tests** for new functionality
4. **Test thoroughly** on your local system
5. **Submit a pull request** with:
   - Clear title and description
   - Reference to any related issues
   - Screenshots for UI changes
   - Test results

### Pull Request Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tests pass locally
- [ ] GUI tested manually
- [ ] CLI tested manually
- [ ] Executables built successfully (if applicable)

## Screenshots (if applicable)
Add screenshots for UI changes

## Additional Notes
Any additional information or context
```

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- **Operating System** and version
- **Python version** (if running from source)
- **Exact error message** or behavior
- **Steps to reproduce** the issue
- **Expected vs. actual behavior**
- **Sample files** (if applicable and safe to share)

### Feature Requests

For feature requests, please include:

- **Clear description** of the feature
- **Use case** or problem it solves
- **Proposed solution** (if you have ideas)
- **Alternative solutions** considered

## Code of Conduct

### Our Standards

- **Be respectful** and inclusive
- **Be patient** with newcomers
- **Provide constructive feedback**
- **Focus on the issue, not the person**
- **Help create a welcoming environment**

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Spam or off-topic discussions
- Sharing private information without permission

## Getting Help

If you need help or have questions:

1. **Check existing documentation** (README, guides, code comments)
2. **Search existing issues** on GitHub
3. **Create a new issue** with your question
4. **Be specific** about what you're trying to achieve

## Recognition

Contributors will be recognized in:
- Project README acknowledgments
- Release notes for significant contributions
- GitHub contributor statistics

Thank you for contributing to Image2PDF Converter! 🎉 
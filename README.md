# PDF Merger Tool

A simple and user-friendly desktop application for merging multiple PDF files into a single document.

**Created by Hamza Zartaj**

## Features

- **Intuitive GUI**: Easy-to-use interface built with Tkinter
- **Multiple File Selection**: Add multiple PDF files at once
- **Drag and Reorder**: Move files up or down to customize merge order
- **File Management**: Remove unwanted files from the merge list
- **Custom Output**: Choose where to save your merged PDF
- **Error Handling**: User-friendly error messages and validation

## Screenshots

The application provides a clean interface with:
- File list display showing selected PDF files
- Add/Remove buttons for file management
- Move Up/Down buttons for reordering
- Merge button to create the final PDF

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Option 1: Run from Source

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python pdf_merger.py
   ```

### Option 2: Use Pre-built Executable

If available, you can download the standalone executable from the releases section and run it directly without installing Python.

## Usage

1. **Launch the application**
   - Run `python pdf_merger.py` or use the executable

2. **Add PDF files**
   - Click "Add PDFs" button
   - Select one or more PDF files from the file dialog

3. **Arrange files (optional)**
   - Select a file in the list
   - Use "Move Up" or "Move Down" to reorder
   - Use "Remove Selected" to remove unwanted files

4. **Merge PDFs**
   - Click "Merge PDFs" button
   - Choose the output location and filename
   - The merged PDF will be saved to your specified location

## Dependencies

- **PyPDF2**: For PDF manipulation and merging
- **tkinter**: For the graphical user interface (included with Python)

## Building Executable

To create a standalone executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller pdf_merger.spec
   ```

The executable will be created in the `dist` folder.

## File Structure

```
pdf-merger/
├── pdf_merger.py          # Main application file
├── requirements.txt       # Python dependencies
├── pdf_merger.spec       # PyInstaller specification
├── icon.ico              # Application icon
├── build/                # Build artifacts (generated)
└── dist/                 # Executable output (generated)
```

## Technical Details

- **Framework**: Python with Tkinter GUI
- **PDF Library**: PyPDF2 for PDF manipulation
- **Build Tool**: PyInstaller for creating executables
- **Compatibility**: Windows, macOS, Linux

## Troubleshooting

### Common Issues

1. **"No PDF files selected" error**
   - Make sure to add at least one PDF file before clicking merge

2. **Permission errors**
   - Ensure you have write permissions to the output directory
   - Close any PDF viewers that might have the files open

3. **Import errors**
   - Install required dependencies: `pip install -r requirements.txt`

### Known Limitations

- Only supports PDF files
- Memory usage increases with large PDF files
- GUI is single-threaded (may become unresponsive with very large files)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is created and maintained by **Hamza Zartaj**. 

This project is open source. Feel free to use and modify as needed, but please give credit to the original author.

## Author

**Hamza Zartaj**
- GitHub: [@Hamza-Zartaj](https://github.com/Hamza-Zartaj)
- Repository: [pdf-merger](https://github.com/Hamza-Zartaj/pdf-merger)

*Developed with ❤️ for simple and efficient PDF management*

## Version History

- **v1.0**: Initial release with basic PDF merging functionality
- GUI interface with file management features
- Executable build support

---

**Note**: This tool is designed for simple PDF merging tasks. For advanced PDF manipulation features, consider using specialized PDF editing software.

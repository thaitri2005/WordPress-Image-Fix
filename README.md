# Image Resizer Tool

A lightweight and portable tool that allows users to resize images to a size of 4.9 MB or less, perfect for uploading to platforms like WordPress. The tool includes an easy-to-use graphical interface for selecting and saving resized images.

## Features

- Resize any `.jpg`, `.jpeg`, `.png`, or `.gif` image to be 4.9 MB or smaller.
- Simple and intuitive GUI using Python's `tkinter` or `PySimpleGUI`.
- Adjustable image compression based on the original size to reduce file size without losing significant quality.
- Saves resized images with custom filenames.
- Portable executable file for easy distribution and use on machines without Python installed.

## Requirements

- **Python 3.x** (for development and running the script before creating the executable)
- **Libraries**:
  - `Pillow` for image processing
  - `tkinter` or `PySimpleGUI` for GUI (depending on the version)

Install the required libraries via pip:

```bash
pip install pillow tkinter PySimpleGUI
```

## Installation

To use the Python script:

Clone the repository:

```bash
git clone https://github.com/yourusername/image-resizer-tool.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python image_resizer.py
```

If you want to create a standalone executable from the Python script, follow the instructions below.

### Create Standalone Executable (Windows)

Install PyInstaller:

```bash
pip install pyinstaller
```

Generate the Executable:

```bash
pyinstaller --onefile --noconsole image_resizer.py
```

The executable will be created in the `dist` folder. You can run the `.exe` file directly on any Windows machine without needing to install Python or any libraries.

## Usage

1. Launch the application by running the Python script or the generated `.exe` file.
2. Click the "Select Image" button to choose the image you want to resize.
3. Specify the output location and filename for the resized image.
4. The tool will automatically resize the image to 4.9 MB or smaller by adjusting the image quality.
5. A message will inform you whether the resize was successful.

## Example

- **Original Image**: example.jpg (6.2 MB)
- **Resized Image**: example_resized.jpg (4.8 MB)

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

### Explanation of Sections:

- **Features**: Highlights the core functionality of your tool.
- **Requirements**: Lists the libraries and tools needed to run the script.
- **Installation**: Step-by-step guide on how to install and run the script, including instructions on creating an executable with PyInstaller.
- **Usage**: Provides details on how to use the tool once installed or downloaded.
- **Example**: Demonstrates a typical use case for better understanding.
- **Contributing**: Invites contributions from other developers.
- **License**: Specifies the license under which your project is shared.

Feel free to customize this template to your liking and add any specific details about your tool.

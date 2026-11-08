🖼️ Image Resizer

A simple Python-based Image Resizer that allows users to resize multiple images by specifying custom width and height dimensions. It uses the Pillow library to process images and automatically saves the resized images in a separate output folder.

✨ Features

- Batch Image Resizing: Resize multiple images automatically.
- Custom Dimensions: Specify your desired width and height.
- Multiple Image Formats: Supports JPG, JPEG, PNG and WEBP formats.
- Input Validation: Accepts only positive integer dimensions.
- Repeated Input Validation: Asks users to enter dimensions again if invalid values are provided.
- Error Handling: Handles image processing errors without stopping the entire program.
- Automatic Output Folder Creation: Creates the output folder if it doesn't already exist.
- Original Filenames: Preserves the original filenames when saving resized images.

🛠️ Technologies Used

- Python
- Pillow (Python Imaging Library)

📂 Project Structure

Image-Resizer/
│
├── input_images/
│   ├── sample_image1.jpeg
│   ├── sample_image2.jpeg
│   └── sample_image3.jpeg
│
├── output_images/
│   └── .gitkeep
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/nainabharti/image-resizer.git

2. Navigate to the project directory

cd image-resizer

3. Create a virtual environment (optional but recommended)

python -m venv .venv

4. Activate the virtual environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1

5. Install the required dependencies

pip install -r requirements.txt

▶️ How to Run

1. Place the images you want to resize inside the "input_images" folder.

2. Run the Python program:

python main.py

3. Enter your desired width and height when prompted.

4. The program will resize the supported images and save them inside the "output_images" folder.

📸 Supported Image Formats

- ".jpg"
- ".jpeg"
- ".png"
- ".webp"

🔮 Future Scope

- Maintain the original aspect ratio while resizing.
- Apply common dimensions to all images without asking repeatedly.
- Add image format conversion.
- Allow users to select custom input and output directories.
- Develop a graphical user interface (GUI).

👩‍💻 Author

Naina Bharti

- GitHub: "@nainabharti" (https://github.com/nainabharti)

---

⭐ If you find this project useful, consider giving it a star!
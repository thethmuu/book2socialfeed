# Book2SocialFeed 📚➡️📱

This Python script extracts text from PDF files, splits it into chunks, and saves the chunks as both JSON and HTML files. It's useful for processing large documents and preparing text data for further analysis or processing, such as creating social media content from books.

## Features 🌟

- Extracts text from PDF files 📄
- Saves text as JSON and HTML files 📊

## Roadmap 🛣️

- [x] Accept input from file explorer.
- [ ] Add a web interface.
- [ ] Improve chunking with AI models.

## Requirements 🛠️

- Python 3.6+
- PyPDF2 library
- PyQt5

## Installation 🚀

1. Clone this repository:

   ```bash
   git clone https://github.com/thethmuu/book2socialfeed.git
   ```

2. Navigate to the project directory:

   ```bash
   cd book2socialfeed
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage 🖥️

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter the following prompts:

   - PDF file name 📁
   - Number of pages to skip (default is 1) ⏭️
   - Chunk size (default is 50) 📏

3. The script generates:
   - `output.json`: Extracted text chunks
   - `output.html`: Basic styled representation of the chunks

## Output 📊

- `output.json` contains an array of text chunks.
- `output.html` displays the text chunks in a simple format.

## Customization ⚙️

Modify `chunk_size` and `skip_pages` in the script for different defaults.

## Contributing 🤝

Contributions and feature requests are welcome! Check the [issues page](https://github.com/thethmuu/book2socialfeed/issues).

## License 📜

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

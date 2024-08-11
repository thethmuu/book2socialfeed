# Book2SocialFeed 📚➡️📱

This Python script extracts text from PDF files, splits it into chunks, and saves the chunks as both JSON and HTML files. It's perfect for processing large documents and preparing text data for further analysis or processing, such as creating social media content from books.

## Features 🌟

- Extracts text from PDF files 📄
- Splits text into manageable chunks 🧩
- Creates JSON output with an array of text chunks 📊
- Generates an HTML file with styled output using Tailwind CSS 🎨

## Roadmap 🛣️

- [ ] Add a web interface to the script.
- [ ] Accept input file from front-end UI.
- [ ] Update to use OpenAI's GPT, Gemini or their equivalent to create more intelligent chunks and social media-friendly content.
- [ ] Serve the dynamic output file via a web server instead of generating a local file.

## Requirements 🛠️

- Python 3.6+
- PyPDF2 library

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

2. Follow the prompts to enter:

   - PDF file name 📁
   - Number of pages to skip (optional, default is 1) ⏭️
   - Chunk size (optional, default is 50) 📏

3. The script will process the PDF and create two output files:
   - `output.json`: Contains the extracted text chunks as a JSON array
   - `output.html`: A visually styled representation of the chunks using Tailwind CSS

## Output 📊

- The `output.json` file contains an array of strings, where each string is a chunk of text from the PDF.
- The `output.html` file provides a visually appealing, responsive web page displaying the text chunks, styled with Tailwind CSS.

## Customization ⚙️

You can modify the default `chunk_size` and `skip_pages` values in the script if you frequently use different values.

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/thethmuu/book2socialfeed/issues).

## License 📜

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

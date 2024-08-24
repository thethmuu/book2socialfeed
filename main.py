import PyPDF2
import json
from tqdm import tqdm
from PyQt5.QtWidgets import QApplication, QFileDialog

def extract_pdf_to_json(pdf_path, output_json_path, skip_pages=1, chunk_size=50):
    content = []
    current_chunk = []
    word_count = 0

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        
        with tqdm(total=total_pages - skip_pages, desc="Processing PDF", unit="page") as pbar:
            for page_num in range(skip_pages, total_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                words = text.split()
                
                for word in words:
                    current_chunk.append(word)
                    word_count += 1
                    
                    if word_count >= chunk_size:
                        chunk_text = ' '.join(current_chunk)
                        content.append(chunk_text)
                        current_chunk = []
                        word_count = 0
                
                pbar.update(1)

    if current_chunk:
        chunk_text = ' '.join(current_chunk)
        content.append(chunk_text)

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)
    
    return content

def save_as_html(chunks):
    chunk_count = len(chunks)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book2SocialFeed Output</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 font-sans">
        <header class="bg-emerald-600 text-white p-4 shadow-md">
            <div class="max-w-3xl mx-auto flex items-center justify-between">
                <h1 class="text-2xl font-bold">Book2SocialFeed</h1>
                <p class="text-white">Total Chunks: {chunk_count}</p>
            </div>
        </header>
        <main class="max-w-3xl mx-auto mt-6 pb-16">
    """
    
    for i, chunk in enumerate(chunks, 1):
        html_content += f"""
            <article class="bg-white rounded-lg shadow-md mb-4 p-4">
                <div class="flex items-center mb-4">
                    <img src="https://via.placeholder.com/40" alt="Profile" class="w-10 h-10 rounded-full mr-3">
                    <div>
                        <h3 class="font-semibold">Book Excerpt</h3>
                        <p class="text-gray-500 text-sm">Posted just now</p>
                    </div>
                </div>
                <p class="text-gray-800 mb-4">{chunk}</p>
                <div class="flex items-center text-gray-500 text-sm">
                    <button class="flex items-center mr-4">
                        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"></path></svg>
                        Like
                    </button>
                    <button class="flex items-center mr-4">
                        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                        Comment
                    </button>
                    <button class="flex items-center">
                        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg>
                        Share
                    </button>
                </div>
            </article>
        """
    
    html_content += """
        </main>
    </body>
    </html>
    """
    
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def get_pdf_file_from_dialog():
    app = QApplication([])  
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(None, "Select PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
    return filename if filename else None

def main():
    pdf_filename = get_pdf_file_from_dialog()  
    if not pdf_filename:
        print("No file selected. Exiting.")
        return
    
    output_filename = "output.json"  

    skip_pages = int(input("Enter the number of pages to skip (default 1): ") or "1")
    chunk_size = int(input("Enter the chunk size (default 50): ") or "50")

    chunks = extract_pdf_to_json(pdf_filename, output_filename, skip_pages, chunk_size)
    save_as_html(chunks)
    
    print(f"Processed {pdf_filename} into {len(chunks)} chunks. Output saved to {output_filename} and output.html")

if __name__ == "__main__":
    main()
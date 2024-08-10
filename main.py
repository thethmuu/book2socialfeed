import PyPDF2
import json
import os

def extract_pdf_to_json(pdf_path, output_json_path, skip_pages=1, chunk_size=50):
    content = []
    current_chunk = []
    word_count = 0

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(skip_pages, len(reader.pages)):
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

    # Add any remaining content
    if current_chunk:
        chunk_text = ' '.join(current_chunk)
        content.append(chunk_text)

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)
    
    return content  # Return the list of chunks

def save_as_html(chunks):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book2SocialFeed Output</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 p-8">
        <div class="max-w-3xl mx-auto">
            <h1 class="text-3xl font-bold mb-6 text-center text-blue-600">Book2SocialFeed Output</h1>
            <div class="space-y-4">
    """
    
    for i, chunk in enumerate(chunks, 1):
        html_content += f"""
                <div class="bg-white p-4 rounded-lg shadow">
                    <h2 class="text-xl font-semibold mb-2 text-gray-700">Chunk {i}</h2>
                    <p class="text-gray-600">{chunk}</p>
                </div>
        """
    
    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def main():
    pdf_filename = input("Enter the PDF filename: ")
    output_filename = "output.json"  # Fixed output filename

    skip_pages = int(input("Enter the number of pages to skip (default 1): ") or "1")
    chunk_size = int(input("Enter the chunk size (default 50): ") or "50")

    chunks = extract_pdf_to_json(pdf_filename, output_filename, skip_pages, chunk_size)
    save_as_html(chunks)
    
    print(f"Processed {pdf_filename} into {len(chunks)} chunks. Output saved to {output_filename} and output.html")

if __name__ == "__main__":
    main()
import PyPDF2
import json

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
    
    return len(content)  # Return the number of chunks

def main():
    pdf_filename = input("Enter the PDF filename: ")
    output_filename = "output.json"  # Fixed output filename

    skip_pages = int(input("Enter the number of pages to skip (default 1): ") or "1")
    chunk_size = int(input("Enter the chunk size (default 50): ") or "50")

    num_chunks = extract_pdf_to_json(pdf_filename, output_filename, skip_pages, chunk_size)
    print(f"Processed {pdf_filename} into {num_chunks} chunks. Output saved to {output_filename}")

if __name__ == "__main__":
    main()
# Import the required libraries
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


# Define a function to extract the text from a PDF file
def extract_text_from_pdf(pdf_path):
    # Create a resource manager to handle the PDF file
    resource_manager = PDFResourceManager()

    # Create a StringIO object to store the extracted text
    output = StringIO()

    # Create a text converter to convert the pages to text and write the text to the StringIO object
    converter = TextConverter(resource_manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(resource_manager, converter)

    # Extract the text from the PDF file
    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
            interpreter.process_page(page)

    # Close the converter and StringIO objects
    converter.close()


    # Return the extracted text as a string
    return output.getvalue()
    output.close()

# Set the directory where the PDF files are located
pdf_dir = 'pdf_files'

# Set the directory where the preprocessed data will be saved
data_dir = 'preprocessed_data'

# Create the data directory if it does not exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Iterate through the PDF files in the directory
for pdf_file in os.listdir(pdf_dir):
    # Extract the text from the PDF file
    pdf_text = extract_text_from_pdf(os.path.join(pdf_dir, pdf_file))

    # Preprocess the text
    processed_text = pdf_text.lower()  # Convert to lowercase
    processed_text = processed_text.replace('.', ' .')  # Add spaces before and after periods
    processed_text = processed_text.replace(',', ' ,')  # Add spaces before and after commas
    processed_text = processed_text.replace('?', ' ?')  # Add spaces before and after question marks
    processed_text = processed_text.replace('!', ' !')  # Add spaces before and after exclamation marks

    # Save the preprocessed text to a file in the data directory
    with open(os.path.join(data_dir, pdf_file + '.txt'), 'w') as f:
        f.write(processed_text)

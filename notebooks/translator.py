from deep_translator import GoogleTranslator

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=4500):
    # Split text into smaller chunks to avoid exceeding the limit
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

# Specify source and target languages
source_language = 'fr'
target_language = 'en'

# Path to the input CSV file
input_csv_file = 'C:\\Users\\tech\\Desktop\\MoroccoEconomyYTAnalysis\\notebooks\\divided_subs.csv'

# Path to the output CSV file for translated data
output_csv_file = 'newtranslated_dataset.csv'

# Read the input CSV file
with open(input_csv_file, 'r', encoding='utf-8') as file:
    csv_contents = file.read()

# Split the CSV contents into smaller chunks
chunks = split_text_into_chunks(csv_contents)

# Initialize an empty list to store translated chunks
translated_chunks = []

# Translate each chunk and store the translations
for chunk in chunks:
    translated_chunk = GoogleTranslator(source=source_language, target=target_language).translate(chunk)
    translated_chunks.append(translated_chunk)

# Combine the translated chunks into a single result
translated_result = ''.join(translated_chunks)

# Save the translated data to the output CSV file
with open(output_csv_file, 'w', encoding='utf-8') as output_file:
    output_file.write(translated_result)

import pandas as pd

# Load your CSV file with the correct encoding (UTF-8)
csv_file = "C:\\Users\\tech\\Desktop\\MoroccoEconomyYTAnalysis\\data\\cleaned_dataset.csv"
df = pd.read_csv(csv_file, encoding="utf-8")

# Define the desired sequence length (512 in your case)
sequence_length = 512

# Initialize lists to store the divided captions
divided_captions = []

# Loop through the captions and divide them
for index, row in df.iterrows():
    caption = row['subtitles']
    caption_length = len(caption)

    # Divide the caption into sequences
    for i in range(0, caption_length, sequence_length):
        # Preserve special characters by using slicing with sequence_length
        sequence = caption[i:i + sequence_length]
        divided_captions.append(sequence)

# Create a new DataFrame with the divided captions
divided_df = pd.DataFrame({'divided_captions': divided_captions})

# Save the divided captions to a new CSV file with UTF-8 encoding
divided_csv_file = "divided_captions.csv"
divided_df.to_csv(divided_csv_file, index=False, encoding="utf-8")

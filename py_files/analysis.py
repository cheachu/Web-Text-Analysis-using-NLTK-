from textblob import TextBlob
import pandas as pd
import syllables
from tqdm import tqdm
# Load input data
input_data = pd.read_excel('Input.xlsx')

# Create an empty DataFrame for output
output_data = pd.DataFrame(columns=[#enter your dataframes here
    ])

for index, row in tqdm(input_data.iterrows(), desc="Processing", total=len(input_data), unit="URL"):
    url_id = row['URL_ID']
    url = row['URL']
    file_path = f'{url_id}.txt'

    # file read
    with open(file_path, 'r', encoding='utf-8') as file:
        article_text = file.read()

    # Perform Text Analysis using TextBlob
    blob = TextBlob(article_text)
    num_sentences = len(blob.sentences)

    # Get the number of words
    num_words = len(blob.words)

    # Get the number of complex words (considering words with more than two syllables as complex)
    num_complex_words = sum(1 for word in blob.words if syllables.estimate(word) > 2)

    # Calculation of each score/length
    positive_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity > 0)
    negative_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity < 0)
    polarity_score = (positive_score - negative_score)/ (( positive_score +negative_score) + 0.000001)
    subjectivity_score = (positive_score +negative_score) / (len(blob.words) + 0.000001)
    avg_sentence_length = (num_words / num_sentences) if num_sentences != 0 else 0

    
    words = blob.words
    
    if len(words) != 0:
        complex_words = [word for word in words if len(word) > 2]  
        percentage_complex_words  = num_complex_words / num_words
    else:
        percentage_complex_words = 0
        complex_words.clear()

    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    avg_words_per_sentence = num_words / num_sentences if num_sentences != 0 else 0

    complex_word_count = len(complex_words)
    word_count = len(words)

    syllable_per_word = sum(syllables.estimate(word) for word in words) / len(words) if len(words) != 0 else 0
   


    personal_pronouns = sum(1 for word in words if word.lower() in ['I', 'we', 'my', 'ours','us'])

    avg_word_length = sum(len(word) for word in words) / len(words) if len(words) != 0 else 0 if len(words) != 0 else 0

    # Append result to output
    output_data = pd.concat([output_data, pd.DataFrame({
        #custom ouput
    })], ignore_index=True)
    

# Save  output file
output_data.to_excel('Output.xlsx', index=False)

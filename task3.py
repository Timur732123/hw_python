# Original text
text = """
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.


"""

# Step 1: Normalize letter cases
sentences = text.split('\n')  # Split by new lines to handle paragraphs separately
normalized_sentences = []

for paragraph in sentences:
    # Split the paragraph into sentences by punctuation marks ('.', '!', '?')
    sentence_parts = paragraph.split('.')
    capitalized_sentences = []

    for sentence in sentence_parts:
        if sentence.strip():  # Check if sentence has content
            # Capitalize the first character and make other characters lowercase
            sentence = sentence.strip().capitalize()
            capitalized_sentences.append(sentence)

    # Join sentences back with periods
    normalized_sentences.append(". ".join(capitalized_sentences))

# Join paragraphs back with new lines
normalized_text = "\n".join(normalized_sentences)

# Step 2: Correct "Iz" when it’s used incorrectly
corrected_text = normalized_text.replace(" iz ", " is ")

# Step 3: Append a sentence with the last words of each sentence
last_words = []

for paragraph in corrected_text.split('\n'):
    for sentence in paragraph.split('. '):
        if sentence:
            last_words.append(sentence.split()[-1].rstrip('.').lower())

# Create the final last-words sentence
last_sentence = " ".join(last_words).capitalize() + "."
corrected_text += "\n" + last_sentence

# Step 4: Count all whitespace characters
whitespace_count = sum(1 for char in corrected_text if char.isspace())

# Display results
print("Normalized and Corrected Text:\n")
print(corrected_text)
print("\nNumber of whitespace characters:", whitespace_count)

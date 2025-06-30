def full_text_preprocessing(text):

    if isinstance(text, list):
        processed_list = []
        for t in text:
            processed_item = full_text_preprocessing(t)
            processed_list.append(processed_item[0])  #extract the from the returned list as recursion output gives final_doc = [[]].
        return processed_list


    #removing hmtl tags (if present), punctions, special chars and numbers
    text = text_preprocessing(text)
    
    #tokenize
    tokens = tokenize(text)

    #remvoing stop words
    cleaned_tokens = stop_words_removal(tokens)

    #lemmatization
    lemmatized = lemmatizer(cleaned_tokens)

    #joining tokens into a single doc for vectorization
    final_doc = final_text(lemmatized)
    
    return [final_doc]
from src.utilities import text_logger, singleton

logger = text_logger.get_logger("create_summary")


def process_text(text):
    sentences = []
    clean_text = ""
    if len(text.split()) > 200:
        logger.info("Text lent greater than 400")
        for item in text.split():
            clean_text += ''.join(item) + " "
            if len(clean_text.split()) > 200:
                if '.' not in item:
                    clean_text += "".join(item) + " "
                else:
                    sentences.append(clean_text)
                    clean_text = ""
    else:
        logger.info("text length lesser than 400 ")
        sentences.append(text)
    return sentences


def get_summary(text, min_len, max_len):
    logger.info("Got request for summary")
    proccesed_data = process_text(text)
    print(len(proccesed_data))
    model = singleton.Singletons.get_instance().get_model()
    tokenizer, device = singleton.Singletons.get_instance().get_tokenizer()
    if max_len > 512:
        logger.info("Got max length greater than sequence length reducing it")
        max_len = 512
    all_summaries = []
    for item in proccesed_data:
        if len(item.split()) < max_len:
            max_len = len(item.split())
            min_len = int(max_len * 0.50)
        tokenized_text = tokenizer.encode("summarize: " + str(item), return_tensors="pt").to(device)
        model_output = model.generate(tokenized_text, max_length=max_len, min_length=min_len, num_beams=1,
                                      no_repeat_ngram_size=2)
        summary = tokenizer.decode(model_output[0])
        print("Text:-{}".format(item))
        print("\n")
        print("summary:{}".format(summary))
        all_summaries.append(summary)
    result = ""
    for item in all_summaries:
        result += "".join(item) + " ."
    return result

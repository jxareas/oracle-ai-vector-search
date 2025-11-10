import os


# FAQ File currently located at: https://oracle-livelabs.github.io/database/ai-chatbot-engine/vectorization/files/faq.txt
# GitHub repository: https://github.com/oracle-livelabs/database

def load_faqs(directory_path):
    faqs = {}

    for filename in os.listdir(directory_path):
        if filename.endswith("faq.txt"):  # assuming FAQs are in .txt files
            file_path = os.path.join(directory_path, filename)
            with open(file_path) as f:
                raw_faq = f.read()

            filename_without_ext = os.path.splitext(filename)[0]  # remove .txt extension
            faqs[filename_without_ext] = [text.strip() for text in raw_faq.split('=====')]

    return faqs

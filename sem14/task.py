import re


def clean_text(text):
    return re.sub(r'[^a-zA-Z ]', '', text).lower()
    # new_text = re.sub(r'[^a-zA-Z ]', '', text).lower()
    # new_text = re.compile('[^a-zA-Z ]')
    # return new_text.sub('', text).lower()
    # return new_text


my_text = "Привет, мир! Как твои дела? Hello, world! What you business? Семинар № 14."
cleaned_text = clean_text(my_text)
print(cleaned_text)

import json

# פתיחת הקובץ JSON וטעינת התוכן שלו למילון
def read_known_words():
    with open('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/terror_transcript_analyze/input/known_words.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data
data = read_known_words()

def list_from_known_words(data):

    single_meaning_dict = {}
    multiple_meanings_dict = {}
    for word, meaning in data["decrypted_meanings"].items():
        if isinstance(meaning, list):
            multiple_meanings_dict[word] = meaning
        else:
            single_meaning_dict[word] = meaning

    additional_context = data.get("additional_context", {})

    participants = additional_context.get("participants", {})
    for key, value in participants.items():
        single_meaning_dict[key] = value
    return single_meaning_dict, multiple_meanings_dict


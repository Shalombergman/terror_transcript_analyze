

def retuen_dict_from_context() :
    with open('/Users/shalom_bergman/kodcode2/Data_engineering_course/Python/terror_transcript_analyze/input/context_score.txt', mode='r', encoding='utf-8') as file:
        dictionary = {}
        for line in file:
            key, value = line.strip().split(':')
            dictionary[key.strip()] = float(value.strip())

    return dictionary
# print(retuen_dict_from_context())

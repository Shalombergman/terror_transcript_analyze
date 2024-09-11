import dict_context_score

words_code = {key:value for key, value in dict_context_score.retuen_dict_from_context().items() if float(value)< 0.25}


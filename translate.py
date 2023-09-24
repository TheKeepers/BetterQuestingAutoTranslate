import openai
import time

openai.api_key = 'put-your-apikey-here'

def translate_text(text, source_language='English', target_language='Chinese Simplified'):
    prompt = f"Translate the following '{source_language}' text to '{target_language}': {text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-instruct",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translation = response.choices[0].message.content.strip()
    return translation


def translate_arr(data_to_translate_arr):
    result_arr = []
    data_wait_to_translate = "\n\n".join(data_to_translate_arr)
    pos = 0
    effective_pos = 0
    translated_pos = -2
    finish = False
    fw = open("test.txt", "w", encoding='utf-8')
    fw.write(data_wait_to_translate)

    while True:
        while True:
            pos = data_wait_to_translate.find("\n\n", pos + 1)
            if pos == -1:
                effective_pos = len(data_wait_to_translate) + 1
                finish = True
                break
            # print(Pos - translated_pos,Pos)
            if pos - translated_pos > 4800:
                break
            effective_pos = pos

        translation_result = translate_text(data_wait_to_translate[translated_pos + 2:effective_pos])
        print(len(data_wait_to_translate[translated_pos + 2:effective_pos].split("\n\n")),
              len(translation_result.split("\n\n")))
        if len(data_wait_to_translate[translated_pos + 2:effective_pos].split("\n\n")) != len(
                translation_result.split("\n\n")):
            print("Fail!!!!!!!!!!!!!")
        result_arr.append(translation_result)
        translated_pos = effective_pos
        if finish:
            print(("\n\n".join(result_arr)).split("\n\n"))
            return ("\n\n".join(result_arr)).split("\n\n")
        time.sleep(8)

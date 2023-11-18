import openai

def generate_text_with_openai(subjectName):

    api_key = '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'

    request = 'generate an 150 words article on any random {subject} category'.format(subject=subjectName)

    # Configure GPT-3 parameters
    response = openai.Completion.create(
        engine="text-davinci-001",  # You can choose other engines like 'text-davinci-003'
        prompt=request,
        max_tokens=150,  # Adjust the desired length of the generated text
        api_key=api_key
    )

    generated_text = response.choices[0].text
    return generated_text
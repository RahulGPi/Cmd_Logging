import google.generativeai as genai
class api:
    # text to send
    prompt_text = """The above lines are history of cmd line read commands, 
    give 10-15 worded description along with the last word in another line to be the risk level of it, 
    if commands are  syntactically wrong, unrecognizable commands, only time stamps; give the risk level as 'LOW',
    do not have any other words then the risk levels
    these risk levels are 'LOW','MED','HIGH'"""
    # API key
    api_key = 'Insert API KEY'
    @classmethod
    def combine(cls, api_send):
        # Combine api_send and prompt_text into the prompt
        combined_prompt = f"{api_send}\n{cls.prompt_text}"

    # Configure the Google Generative AI
        genai.configure(api_key=cls.api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content using the combined prompt
        response = model.generate_content(combined_prompt)
        return response
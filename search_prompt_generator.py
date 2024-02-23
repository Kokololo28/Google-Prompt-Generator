# search_prompt_generator.py

def generate_google_search_prompts(keywords):
    prompts = [f"Google search: {keyword}" for keyword in keywords]
    return prompts

if __name__ == "__main__":
    search_keywords = ["Python programming", "Machine learning", "GitHub tutorial"]
    prompts = generate_google_search_prompts(search_keywords)

    for prompt in prompts:
        print(prompt)

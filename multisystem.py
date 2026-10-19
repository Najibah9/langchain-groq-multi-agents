import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


def research_agent(topic):
    prompt = f"""
    You are a helpful assistant summarize your research in less than 500 words include real life examples and references.
     Topic: {topic}.
    """
    response = llm.invoke(prompt)
    return response.content


def review_agent(research):
    prompt = f"""
You are a helpful reviewer that can review research and provide feedback. Please provide a summary of the research, highlight any strengths and weaknesses, and suggest areas for improvement.
Research: {research}
    """
    response = llm.invoke(prompt)
    return response.content


def multisystem_agent(topic):
    research = research_agent(topic)
    print("----Output of 1st Agent----")
    print(research)

    final_output = review_agent(research)
    print("----Output of 2nd Agent----")
    print(final_output)


if __name__ == "__main__":
    multisystem_agent(input("Enter a topic to research: "))
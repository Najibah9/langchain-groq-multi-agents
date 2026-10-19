import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


def writer_agent(topic: str) -> str:
    prompt = f"""
You are an expert research writer and analyst. Your task is to produce a rigorous, comprehensive research summary on the topic below.

### Topic:
{topic}

### Instructions:
1. Length: Keep the summary strictly between 350 and 500 words.
2. Structure:
   - Executive Overview: 2-3 sentences framing the core premise.
   - Key Findings & Mechanisms: The primary drivers or concepts.
   - Real-World Case Studies / Examples: At least 2 named, specific real-world examples illustrating the topic in practice.
   - Future Outlook / Key References: Mention key organizations, studies, or industry benchmarks associated with this topic.
3. Tone: Authoritative, objective, and analytically sharp. Avoid vague filler language.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def reviewer_agent(draft: str) -> str:
    prompt = f"""
You are a senior peer reviewer and fact auditor. Critically evaluate the research draft provided below. Do NOT rewrite the article; your job is strictly to deliver actionable, analytical critique.

### Research Draft:
{draft}

### Evaluation Criteria:
1. Accuracy & Depth: Are the claims supported? Are the real-world examples concrete or superficial?
2. Logical Flow: Does the narrative progress logically from premise to conclusion?
3. Blind Spots: What critical perspectives, counterarguments, or recent developments were omitted?

### Output Format:
- Strengths: (2-3 bullet points on what works well)
- Critical Weaknesses & Gaps: (2-3 specific issues or missing context)
- Actionable Directives for Editor: (Numbered, concrete instructions on what to add, cut, or rephrase)
"""
    response = llm.invoke(prompt.strip())
    return response.content


def editor_agent(draft: str, review_feedback: str) -> str:
    prompt = f"""
You are a senior copy editor and publishing director. Your task is to synthesize the original draft and the reviewer's critique into a polished, publication-ready final piece.

### Original Draft:
{draft}

### Reviewer Feedback & Directives:
{review_feedback}

### Editorial Rules:
1. Implement the reviewer's actionable directives without losing the writer's core voice.
2. Fix any awkward phrasing, tighten passive voice, and eliminate redundancy.
3. Ensure named references and examples flow naturally within the prose.
4. Maintain a clean, professional layout using Markdown headings and bullet points where appropriate.

### Output:
Return ONLY the finalized, publication-ready article, followed by a brief 2-bullet summary of key editorial changes at the very bottom.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def multisystem_agent(topic: str):
    print("=" * 60)
    print("STEP 1: WRITER AGENT (Generating Draft)")
    print("=" * 60)
    draft = writer_agent(topic)
    print(draft)

    print("\n" + "=" * 60)
    print("STEP 2: REVIEWER AGENT (Auditing & Feedback)")
    print("=" * 60)
    feedback = reviewer_agent(draft)
    print(feedback)

    print("\n" + "=" * 60)
    print("STEP 3: EDITOR AGENT (Final Publication)")
    print("=" * 60)
    final_output = editor_agent(draft, feedback)
    print(final_output)


if __name__ == "__main__":
    user_topic = input("Enter a topic to research: ").strip()
    if user_topic:
        multisystem_agent(user_topic)
    else:
        print("Topic cannot be empty.")
        print("Topic cannot be empty.")
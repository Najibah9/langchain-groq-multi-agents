import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


def product_search_agent(query: str, budget: str) -> str:
    prompt = f"""
You are an expert Product Discovery Specialist. Your task is to identify 2 to 3 distinct product candidates matching the user's requirements.

### User Request:
- Query: {query}
- Target Budget: {budget}

### Instructions:
1. Provide 2-3 specific, real-world product models that match the specifications.
2. For each product, list:
   - Full Model Name & Approximate Market Price
   - Core Specifications & Standout Features
   - Intended User Profile (who it is best for)
3. Keep descriptions factual, structured, and concise.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def price_budget_analyst(products: str, budget: str) -> str:
    prompt = f"""
You are a Financial & Price Analyst specializing in consumer goods. Evaluate the pricing and economic value of the candidate products relative to the user's budget.

### Target Budget:
{budget}

### Candidate Products:
{products}

### Instructions:
1. Budget Fit: Categorize each product as Under Budget, On Budget, or Over Budget.
2. Value-for-Money Metric: Assess whether premium features justify any extra cost or if cheaper alternatives provide better value.
3. Cost-to-Lifespan: Highlight potential hidden costs (maintenance, accessories, longevity).
4. Output a concise comparative cost-benefit breakdown.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def review_analyst(products: str) -> str:
    prompt = f"""
You are a Consumer Sentiment & Quality Assurance Analyst. Analyze the real-world user sentiment and reliability records for the candidate products.

### Candidate Products:
{products}

### Instructions:
For each product, break down:
1. Common Praises: Top 2-3 recurring positive remarks from long-term owners.
2. Frequent Pain Points: Top 2-3 common complaints, build quality flaws, or software glitches.
3. Durability & Reliability Risk: Low, Medium, or High risk based on failure rates and customer support responsiveness.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def recommendation_analyst(
    products: str, price_analysis: str, review_analysis: str
) -> str:
    prompt = f"""
You are the Chief Shopping Advisor and Final Decision Strategist. Synthesize the findings from product discovery, price analysis, and review audits into a final purchasing directive.

### Discovered Products:
{products}

### Price & Budget Assessment:
{price_analysis}

### Consumer Reviews & Reliability Audit:
{review_analysis}

### Instructions:
1. Provide a definitive, ranked hierarchy (1st Place, Runner-Up, Alternative).
2. For the Top Pick, provide a direct, punchy justification on why it wins overall.
3. Provide a clear "Buy If / Skip If" rule for each option to help the user decide instantly.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def shopping_agent_pipeline(query: str, budget: str):
    print("=" * 60)
    print("AGENT 1: PRODUCT SEARCH (Finding Candidates)")
    print("=" * 60)
    products = product_search_agent(query, budget)
    print(products)

    print("\n" + "=" * 60)
    print("AGENT 2: PRICE & BUDGET ANALYST (Evaluating Value)")
    print("=" * 60)
    price_eval = price_budget_analyst(products, budget)
    print(price_eval)

    print("\n" + "=" * 60)
    print("AGENT 3: REVIEW ANALYST (Auditing Sentiments & Flaws)")
    print("=" * 60)
    review_eval = review_analyst(products)
    print(review_eval)

    print("\n" + "=" * 60)
    print("AGENT 4: RECOMMENDATION ANALYST (Final Verdict)")
    print("=" * 60)
    final_verdict = recommendation_analyst(products, price_eval, review_eval)
    print(final_verdict)


if __name__ == "__main__":
    search_query = input("Enter product to search for: ").strip()
    user_budget = input("Enter your budget (e.g., $500, under $1000): ").strip()

    if search_query:
        shopping_agent_pipeline(search_query, user_budget or "Flexible")
    else:
        print("Product query cannot be empty.")
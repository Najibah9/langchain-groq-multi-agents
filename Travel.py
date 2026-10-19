import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


def destination_researcher(trip_details: str) -> str:
    prompt = f"""
You are a Destination Research Specialist. Your task is to identify and curate the best attractions and experiences tailored to the user's trip request.

### Trip Details:
{trip_details}

### Instructions:
1. Identify 6 to 8 top sights, landmarks, and cultural spots matching the duration and traveler profile.
2. Group the recommendations geographically or by proximity to minimize travel time.
3. For each attraction, note:
   - Highlight / Why visit
   - Approximate entry fees and ideal visiting time (e.g., sunrise, afternoon, sunset)
4. Keep the list focused, structured, and free of fluff.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def budget_planner(trip_details: str, places_research: str) -> str:
    prompt = f"""
You are an expert Travel Financial Analyst and Budget Planner. Your job is to calculate and allocate expenses realistically against the user's stated budget.

### Trip Details:
{trip_details}

### Recommended Places & Sightseeing:
{places_research}

### Instructions:
1. Provide a detailed, category-wise cost breakdown:
   - Stay / Accommodation (per night & total)
   - Food & Dining (per day per person & total)
   - Local Transport (auto-rickshaws, cabs, or scooter rentals)
   - Sightseeing & Activity Fees (monument tickets, boat rides, etc.)
   - Contingency / Buffer Fund (at least 10%)
2. State the estimated total vs. the target budget.
3. Classify the spending profile (Budget, Moderate, or Luxury) and flag any areas prone to overspending.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def itinerary_planner(
    trip_details: str, places_research: str, budget_breakdown: str
) -> str:
    prompt = f"""
You are a Professional Itinerary Architect. Create a smooth, hour-by-hour or slot-by-slot daily schedule based on the destination research and budget allocations.

### Trip Details:
{trip_details}

### Destination Highlights:
{places_research}

### Budget Allocation:
{budget_breakdown}

### Instructions:
1. Organize the trip day-by-day (Day 1, Day 2, Day 3, etc.).
2. For each day, divide into:
   - Morning (exploration, active sightseeing)
   - Afternoon (indoor sights, leisurely meals, break)
   - Evening / Sunset (scenic views, cultural shows, markets)
3. Ensure the schedule is geographically logical (no zigzagging across the city) and respects travel pacing.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def travel_reviewer(
    trip_details: str,
    places_research: str,
    budget_breakdown: str,
    itinerary: str,
) -> str:
    prompt = f"""
You are a Senior Travel Quality Auditor and Local Expert. Critically evaluate the complete travel plan for practicality, pacing, and financial feasibility.

### Trip Details:
{trip_details}

### Budget Breakdown:
{budget_breakdown}

### Proposed Itinerary:
{itinerary}

### Instructions:
1. Feasibility & Pacing Check: Are days too packed or rushed? Are opening hours respected?
2. Budget Realism: Is the estimated spend realistic for the destination and party size?
3. Practical Travel Tips & Warnings:
   - Local scams or overcharging traps to avoid
   - Advance booking alerts (tickets, permits, peak crowd slots)
   - Dress code, cultural etiquette, or weather-specific tips
4. Final Verdict: Rate the plan (Approved / Needs Adjustment) with a 2-sentence summary.
"""
    response = llm.invoke(prompt.strip())
    return response.content


def travel_planner_pipeline(trip_details: str):
    print("=" * 65)
    print("AGENT 1: DESTINATION RESEARCHER (Curating Attractions)")
    print("=" * 65)
    places = destination_researcher(trip_details)
    print(places)

    print("\n" + "=" * 65)
    print("AGENT 2: BUDGET PLANNER (Allocating Expenses)")
    print("=" * 65)
    budget = budget_planner(trip_details, places)
    print(budget)

    print("\n" + "=" * 65)
    print("AGENT 3: ITINERARY PLANNER (Daily Day-by-Day Schedule)")
    print("=" * 65)
    itinerary = itinerary_planner(trip_details, places, budget)
    print(itinerary)

    print("\n" + "=" * 65)
    print("AGENT 4: TRAVEL REVIEWER (Feasibility, Risks & Final Verdict)")
    print("=" * 65)
    review = travel_reviewer(trip_details, places, budget, itinerary)
    print(review)


if __name__ == "__main__":
    default_request = (
        "Plan a 3-day trip to Udaipur for 2 people with a budget of ₹20,000."
    )
    user_request = input(
        f"Enter trip details [Press Enter for default: '{default_request}']:\n"
    ).strip()

    trip_query = user_request if user_request else default_request
    travel_planner_pipeline(trip_query)
from langchain_core.prompts import ChatPromptTemplate

def get_packing_list_prompt():
    """Returns a ChatPromptTemplate for generating packing lists."""
    system = "You are a helpful travel assistant skilled at creating concise packing lists."
    human = """
    Generate a packing list for a {duration} {trip_type} trip with {weather} weather.
    Include essential items and one optional item with a brief reason (e.g., "Bug spray if near water").
    Output in JSON format with fields: essentials (list), optional (dict with item and reason).
    """
    return ChatPromptTemplate.from_messages([("system", system), ("human", human)])
from connection import config
from agents import Agent, Runner, function_tool
import requests
import json
from typing import List

@function_tool
def product_store()-> List: 
    """
    Fetch product details from the ecommerce API.
    """

    url = "https://next-ecommerce-template-4.vercel.app/api/product"

    try:
        response = requests.get(url) # Make API request
        response.raise_for_status()  # Raise exception for bad status codes
        products = response.json() # Parse JSON response
        return {'status': 'success', 'data': products}

    except requests.RequestException as e:
        return [{"error": f"Failed to fetch products: {str(e)}"}]
    
    except json.JSONDecodeError:
        return [{"error": "Invalid response format from API"}]

# Shopping Agent
shopping_agent = Agent(
    name= "Shopping Agent",
    instructions= """You are a helpful shopping agents..
                  Answer user query related to products by 
                  using 'product_store' tool.. 
                  Beyond products, do not hallucination,
                  Present product in formal format and show each product and its details by breaking line""",
    tools= [product_store]
)

#Example execution
response = Runner.run_sync(
    shopping_agent,
    input= "Get products list with details",                  #---->OK
    #input= "Get products in the chairs category",             ---->OK
    #input= "Tell me product details list",                    ---->OK
    #input= "Get products prices ",                            ---->OK
    #input= "Get products description list",                   ---->OK
    #input= "Recommend some chairs",                           ---->OK
    #input= "What are the details of the most expensive chair?",--->OK
    #input= "Show me all sofas in the shop",                   ---->OK
    #input= "Get details for the Modern Office Chair",         ---->OK
    #input= "Find chairs under $100",                          ---->OK
    #input= "Recommend some dining tables",                    ---->OK
    #input= "Is the Ergonomic Chair in stock?",                ---->OK
    #input= "Compare prices of sofas",                         ---->OK
    #input= "Show me chairs with free shipping",               ---->OK
    #input= "What are the top 3 most expensive products?",     ---->OK
    #input= "Find wooden tables",                              ---->OK
    #input= "How many chairs are available?",                 # ---->OK
    #input= "Get products category",                           ---->Failed
    #input= "How many categories are there in the shop ?",     ---->Failed
    run_config=config
)

print(response.final_output)
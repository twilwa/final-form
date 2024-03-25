from markdown2 import markdown
from markupsafe import Markup
from app.services.gemini_service import GeminiService
# from app.pipelines.newsletter_pipeline import execute_newsletter_pipeline


def generate_newsletter_from_query(query):
    # Fetch or generate your newsletter as Markdown
    newsletter_md = "# Newsletter Title\n\nSome content for **query**: " + query
    newsletter_html = markdown(newsletter_md)
    # Ensure that the HTML is marked safe for rendering in the template
    return Markup(newsletter_html)

# def generate_newsletter_from_query(query):
    # gemini_service = GeminiService()

    # Use Gemini to determine the calls to make to the Dagster pipeline
    # pipeline_instructions = gemini_service.generate_content(f"Based on the query '{query}', what steps should be taken to fetch and process the relevant data using the Dagster pipeline?")

    # Execute the Dagster pipeline based on the instructions
    # pipeline_result = execute_newsletter_pipeline(pipeline_instructions)

    # Use Gemini to enrich and present the pipeline result in markdown format
    # newsletter_content = gemini_service.generate_content(f"Given the following data from the Dagster pipeline:\n{pipeline_result}\n\nGenerate a newsletter in markdown format that presents this information to the user based on their query '{query}'.")

    # return newsletter_content
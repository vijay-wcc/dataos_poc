from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

llm = Ollama(model="llama2")


def rate_issue(description: str):
    response_schemas = [
        ResponseSchema(name="status", description="Red Amber Or Green"),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    format_instructions = output_parser.get_format_instructions()

    prompt = PromptTemplate(
        template="""
        Given the description RAG rate the issue\n{format_instructions}\n{description}
       """,
        input_variables=["description"],
        partial_variables={"format_instructions": format_instructions},
    )

    chain = prompt | llm | output_parser

    return chain.invoke({"description": description})

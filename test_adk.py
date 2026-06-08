import asyncio

from dotenv import load_dotenv
from google.genai import types

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from agents.soil_agent import soil_agent
from agents.fungus_agent import fungus_agent

load_dotenv()


session_service = InMemorySessionService()

soil_runner = Runner(
    agent=soil_agent,
    app_name="smart_soil",
    session_service=session_service
)

fungus_runner = Runner(
    agent=fungus_agent,
    app_name="smart_soil",
    session_service=session_service
)


async def get_agent_response(
    runner,
    session_id,
    user_id,
    text
):

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text=text
            )
        ]
    )

    final_text = None

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message
    ):

        if (
            event.content
            and event.content.parts
            and hasattr(
                event.content.parts[0],
                "text"
            )
        ):
            final_text = (
                event.content.parts[0].text
            )

    return final_text

async def main():

    user_id = "smart_soil_user"

    soil_session = await session_service.create_session(
        app_name="smart_soil",
        user_id=user_id
    )

    fungus_session = await session_service.create_session(
        app_name="smart_soil",
        user_id=user_id
    )

    soil_data = """
    {
        "ph": 5.1,
        "nitrogenio": 12,
        "fosforo": 10,
        "potassio": 15,
        "materia_organica": 1.2
    }
    """

    print("\n===== SENSOR =====")
    print(soil_data)

    soil_response = await get_agent_response(
        soil_runner,
        soil_session.id,
        user_id,
        soil_data
    )

    print("\n===== SOIL AGENT =====")
    print(soil_response)

    fungus_response = await get_agent_response(
        fungus_runner,
        fungus_session.id,
        user_id,
        soil_response
    )

    print("\n===== FUNGUS AGENT =====")
    print(fungus_response)


if __name__ == "__main__":
    asyncio.run(main())
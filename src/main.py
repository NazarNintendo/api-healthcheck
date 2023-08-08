import asyncio

from data import APIState, load_data
from ping import create_job


async def main() -> None:
    """
    Main function to run the program.
    Load the data, create the APIState object, and create the jobs.
    Run the jobs concurrently.
    :return: None
    """
    apis = load_data()
    state = APIState([api.id for api in apis])
    jobs = [create_job(state, api) for api in apis]
    await asyncio.gather(*jobs)


asyncio.run(main())

import asyncio
import os
from httpx import AsyncClient
from dotenv import load_dotenv


class TheirStackAPI:
    def __init__(self, client: AsyncClient):
        self.client = client
        self.api_key = os.getenv("THEIRSTACK_API_KEY")
        self.base_url = "https://api.theirstack.com/v1"

    async def get_jobs(self, page: int, limit: int):
        response = await self.client.post(
            f"{self.base_url}/jobs/search",
            headers={
                "Authorization": f"Bearer {self.api_key}",
            },
            json={
                "posted_at_max_age_days": 1,
                "page": page,
                "limit": limit,
            },
        )
        return response


if __name__ == "__main__":
    load_dotenv()

    for page in [0, 1]:
        response = asyncio.run(TheirStackAPI(AsyncClient()).get_jobs(page, 3))
        print(f"Page {page}")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.json()}")

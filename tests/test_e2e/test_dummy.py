from http import HTTPStatus

import pytest


@pytest.mark.asyncio
class TestDummy:
    async def test_health(self, make_request):
        response = await make_request(method="GET", url=f"/")
        assert response.status == HTTPStatus.OK

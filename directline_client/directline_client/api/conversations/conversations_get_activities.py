from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_set import ActivitySet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: str,
    *,
    watermark: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["watermark"] = watermark

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v3/directline/conversations/{conversation_id}/activities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActivitySet, Any]]:
    if response.status_code == 200:
        response_200 = ActivitySet.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ActivitySet, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    watermark: Union[Unset, str] = UNSET,
) -> Response[Union[ActivitySet, Any]]:
    """Get activities in this conversation. This method is paged with the 'watermark' parameter.

    Args:
        conversation_id (str):
        watermark (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivitySet, Any]]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        watermark=watermark,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    watermark: Union[Unset, str] = UNSET,
) -> Optional[Union[ActivitySet, Any]]:
    """Get activities in this conversation. This method is paged with the 'watermark' parameter.

    Args:
        conversation_id (str):
        watermark (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivitySet, Any]
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        watermark=watermark,
    ).parsed


async def asyncio_detailed(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    watermark: Union[Unset, str] = UNSET,
) -> Response[Union[ActivitySet, Any]]:
    """Get activities in this conversation. This method is paged with the 'watermark' parameter.

    Args:
        conversation_id (str):
        watermark (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivitySet, Any]]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        watermark=watermark,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    watermark: Union[Unset, str] = UNSET,
) -> Optional[Union[ActivitySet, Any]]:
    """Get activities in this conversation. This method is paged with the 'watermark' parameter.

    Args:
        conversation_id (str):
        watermark (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivitySet, Any]
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            watermark=watermark,
        )
    ).parsed

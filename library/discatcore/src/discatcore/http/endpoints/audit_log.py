# SPDX-License-Identifier: MIT

# this file was auto-generated by scripts/generate_endpoints.py

import discord_typings as dt

from ...types import Unset, UnsetOr
from ..route import Route
from .core import EndpointMixin

__all__ = ("AuditLogEndpoints",)


class AuditLogEndpoints(EndpointMixin):
    def get_guild_audit_log(
        self,
        guild_id: dt.Snowflake,
        *,
        user_id: UnsetOr[dt.Snowflake] = Unset,
        action_type: UnsetOr[dt.AuditLogEvents] = Unset,
        before: UnsetOr[dt.Snowflake] = Unset,
        limit: UnsetOr[int] = Unset,
    ):
        return self.request(
            Route("GET", "/guilds/{guild_id}/audit-logs", guild_id=guild_id),
            query_params={
                "user_id": user_id,
                "action_type": action_type,
                "before": before,
                "limit": limit,
            },
        )

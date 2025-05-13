# -* coding: utf-8 -*-
# spacing: 4 spaces

import logging
from mcp.server.fastmcp import FastMCP

class MCPServerSpawner:
    """Class to spawn a FastMCP server for weather alerts."""

    def __init__(self):
        """Initialize the MCPServerSpawner with the server name."""
        self._server_registry = {
            "weather": None,
        }

    def spawn_server(self, name: str) -> FastMCP:
        """Get the FastMCP server instance."""
        if name not in self._server_registry:
            raise ValueError(f"Server '{name}' is not registered.")
        else:
            if self._server_registry[name] is None:
                exec(
                    f"from sandbox.mcp.servers.{name} import get_server; self._server_registry[name] = get_server()",
                    globals(),
                    locals(),
                )
            else:
                logging.warning(f"Server '{name}' is already spawned. Returning existing instance.")
            return self._server_registry[name]


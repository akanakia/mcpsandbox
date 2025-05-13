# -* coding: utf-8 -*-
# spacing: 4 spaces
import logging
import click
from sandbox.mcp.servers import MCPServerSpawner

@click.command()
@click.option(
    "-s",
    "--mcp-server",
    required=True,
    help="Name of the server to spawn.",
)
def _main(mcp_server: str):
    """Main function to run the server."""
    # Get the FastMCP server instance
    spawner = MCPServerSpawner()
    mcp = spawner.spawn_server(mcp_server)

    # Run the server with standard input/output transport
    mcp.run(transport='stdio')

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s [%(levelname)s] | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("server.log")
        ]
    )
    _main()

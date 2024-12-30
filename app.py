import httpx
from agents import agents_list
from phi.playground import Playground

app = Playground(agents=agents_list).get_app()

limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(timeout=5.0, read=15.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)


@app.on_event("shutdown")
async def shutdown_event():
    print("shutting down...")
    await client.aclose()

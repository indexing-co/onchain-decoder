import asyncio
import os
import tornado


from handlers.health_checks import health_check_handlers


PORT = os.environ.get("PORT", 8080)


def make_app():
    return tornado.web.Application(
        health_check_handlers,
    )


async def main():
    app = make_app()
    app.listen(PORT)

    print(f"Listening on port {PORT}")

    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    asyncio.run(main())

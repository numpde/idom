import asyncio

from idom import component, html, run, use_state


@component
def Counter():
    number, set_number = use_state(0)

    async def handle_click(event):
        await asyncio.sleep(3)
        set_number(number + 1)

    return html.div(
        html.h1(number),
        html.button("Increment", on_click=handle_click),
    )


run(Counter)

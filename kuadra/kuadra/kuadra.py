"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="red",
            border_radius="1",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2"),
        rx.button(
            "Increment",
            color_scheme="green",
            border_radius="1",
            on_click=State.icrement,
        )
    )


app = rx.App()
app.add_page(index)

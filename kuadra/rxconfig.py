import reflex as rx

config = rx.Config(
    app_name="kuadra",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
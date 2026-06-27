import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    # Build optional sections using Python conditionals (static data, not reactive state)
    tech_section = (
        rx.flex(
            *[
                rx.badge(
                    rx.box(class_name=technology.icon),
                    technology.name,
                    color_scheme="gray"
                )
                for technology in info.technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        )
        if info.technologies
        else rx.fragment()
    )

    link_buttons = []
    if info.url:
        link_buttons.append(icon_button("link", info.url))
    if info.github:
        link_buttons.append(icon_button("code_xml", info.github))

    image_section = (
        rx.image(
            src=info.image,
            height=IMAGE_HEIGHT,
            width="auto",
            border_radius=EmSize.DEFAULT.value,
            object_fit="cover"
        )
        if info.image
        else rx.fragment()
    )

    side_items = []
    if info.date:
        side_items.append(rx.badge(info.date))
    if info.certificate:
        side_items.append(
            icon_button("shield-check", info.certificate, solid=True)
        )

    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                tech_section,
                rx.hstack(*link_buttons),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        image_section,
        rx.vstack(
            *side_items,
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )

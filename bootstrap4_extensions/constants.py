BUTTON_TAGS = (
    ("a", "Link"),
    ("button", "Button"),
    ("input", "Input"),
    ("submit", "Submit"),
    ("reset", "Reset"),
)
BUTTON_CLASSES = (
    ("btn-primary", "Primary"),
    ("btn-secondary", "Secondary"),
    ("btn-success", "Success"),
    ("btn-danger", "Danger"),
    ("btn-warning", "Warning"),
    ("btn-info", "Info"),
    ("btn-light", "Light"),
    ("btn-dark", "Dark"),
    ("btn-link", "Link"),
)
BUTTON_SIZES = (("sm", "Small"), ("lg", "Large"))
LINK_TARGET_CHOICES = (
    ("_self", "Same Tab/Window (normal)"),
    ("_blank", "New Tab/Window"),
    ("_parent", "Parent Frame"),
    ("_top", "Full Window (break frames)"),
)

NAV_STYLE_CHOICES = (
    ("", "Default Nav"),
    ("nav-tabs", "Tabs"),
    ("nav-pills", "Pills"),
    ("nav-fill", "Fill and Justify"),
)

CONTENT_START = "justify-content-start"
CONTENT_CENTER = "justify-content-center"
CONTENT_RIGHT = "justify-content-end"
NAV_ALIGNMENT_CHOICES = (
    (CONTENT_START, "Left Aligned"),
    (CONTENT_CENTER, "Center Aligned"),
    (CONTENT_RIGHT, "Right Aligned"),
)

NAVBAR_DARK = "navbar-dark"
NAVBAR_LIGHT = "navbar-light"
NAVBAR_BACKGROUND_SCHEME = (
    (NAVBAR_DARK, "Dark Background"),
    (NAVBAR_LIGHT, "Light Background"),
)
NAVBAR_POSITIONS = (
    ("", "Normal"),
    ("fixed-top", "Fixed top"),
    ("fixed-bottom", "Fixed bottom"),
)

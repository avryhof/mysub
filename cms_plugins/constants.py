AUTHENTICATED_USERS = "authenticated_users"
UNAUTHENTICATED_USERS = "unauthenticated_users"
AUTH_USER_CHOICES = (
    (AUTHENTICATED_USERS, "Users who are logged in."),
    (UNAUTHENTICATED_USERS, "Users who are not logged in.")
)

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
BUTTON_SIZES = (
    ("sm", "Small"),
    ("lg", "Large")
)
LINK_TARGET_CHOICES = (
    ("_self", "Same Tab/Window (normal)"),
    ("_blank", "New Tab/Window"),
    ("_parent", "Parent Frame"),
    ("_top", "Full Window (break frames)"),
)
BLOCK_TAGS = (
    ("article", "ARTICLE"),
    ("aside", "ASIDE"),
    ("container", "CONTAINER"),
    ("div", "DIV"),
    ("footer", "FOOTER"),
    ("header", "HEADER"),
    ("hgroup", "HGROUP"),
    ("main", "MAIN"),
    ("section", "SECTION"),
)
TEXT_CLASSES = (
    ("text-primary", "Primary (blue)"),
    ("text-secondary", "Secondary (dark gray)"),
    ("text-success", "Success (green)"),
    ("text-danger", "Danger (red)"),
    ("text-warning", "Warning (yellow)"),
    ("text-info", "Info (turquoise)"),
    ("text-light", "Light (white)"),
    ("text-dark", "Dark (black)"),
    ("text-body", "Body (default color)"),
    ("text-muted", "Muted (gray)"),
    ("text-white", "White"),
    ("text-black-50", "50% Black"),
    ("text-white-50", "50% White"),
)
BACKGROUND_CLASSES = (
    ("bg-primary", "Primary (blue)"),
    ("bg-secondary", "Secondary (dark gray)"),
    ("bg-success", "Success (green)"),
    ("bg-danger", "Danger (red)"),
    ("bg-warning", "Warning (yellow)"),
    ("bg-info", "Info (turquoise)"),
    ("bg-light", "Light (white)"),
    ("bg-dark", "Dark (black)"),
    ("bg-transparent", "Transparent"),
    ("bg-gradient-primary", "Primary Gradient (blue)"),
    ("bg-gradient-secondary", "Secondary Gradient (dark gray)"),
    ("bg-gradient-success", "Success Gradient (green)"),
    ("bg-gradient-danger", "Danger Gradient (red)"),
    ("bg-gradient-warning", "Warning Gradient (yellow)"),
    ("bg-gradient-info", "Info Gradient (turquoise)"),
    ("bg-gradient-light", "Light Gradient (white)"),
    ("bg-gradient-dark", "Dark Gradient (black)"),
)
BACKGROUND_SIZE_AUTO = "auto"
BACKGROUND_SIZE_PERCENTAGE = "percentage"
BACKGROUND_SIZE_COVER = "cover"
BACKGROUND_SIZE_CONTAIN = "contain"
BACKGROUND_SIZE_CHOICES = (
    (BACKGROUND_SIZE_AUTO, "Display the image at it's original size."),
    (BACKGROUND_SIZE_COVER, "Resize the image to cover the entire container."),
    (BACKGROUND_SIZE_CONTAIN, "Resize the image to make sure it is fully visible."),
    (BACKGROUND_SIZE_PERCENTAGE, "Set a Percentage to zoom the image to."),
)
HEADING_TYPES = (
    ("h1", "Heading 1"),
    ("h2", "Heading 2"),
    ("h3", "Heading 3"),
    ("h4", "Heading 4"),
    ("h5", "Heading 5"),
    ("h6", "Heading 6"),
)

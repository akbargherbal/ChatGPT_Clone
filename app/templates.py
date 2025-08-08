def create_ai_message(message_text: str) -> str:
    """
    Creates an HTML snippet for an AI message with Tailwind CSS classes.
    """
    html_content = f"""<div class="prose">
    <p>{message_text}</p>
</div>
"""
    return html_content

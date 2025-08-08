def create_ai_message(message_text: str, model_name: str) -> str:
    """
    Creates an HTML snippet for an AI message with theme-aware Tailwind CSS classes.
    """
    base_classes = "ml-4 p-4 rounded-lg max-w-lg prose prose-sm dark:prose-invert transition-all"
    
    theme_classes = {
        "pro": "bg-white dark:bg-gray-800",
        "flash": "bg-white dark:bg-gray-800 border-l-4 border-cyan-400 shadow-lg",
    }
    
    additional_classes = theme_classes.get(model_name, "")
    
    combined_classes = f"{base_classes} {additional_classes}".strip()

    html_content = f"""<div class="{combined_classes}">
    <p>{message_text}</p>
</div>
"""
    return html_content

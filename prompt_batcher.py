"""
ComfyUI Simple Prompt Batcher with Global Style (Robust Version)
Takes multiple prompts (one per line) and appends a global style to all prompts for batch processing
Includes extra safeguards to prevent duplicate prompts or ComfyUI misinterpretation
"""

class SimplePromptBatcher:
    """
    Simple prompt batcher - one prompt per line
    Automatically batches through all prompts for inference
    Allows a global style to be appended to all prompts
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Prompts (one per line). Enter one prompt per line. No empty lines between prompts.",
                    "tooltip": "Each line is treated as a separate prompt for batch processing."
                }),
                "style": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Global Style. Optional: style string appended to all prompts.",
                    "tooltip": "Define a style prompt that gets appended to every prompt in the list."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "batch_prompts"
    CATEGORY = "utils/text"
    OUTPUT_IS_LIST = (True,)  # This makes it output as a batch

    def batch_prompts(self, prompts, style=""):
        """
        Split prompts by newline and return as batch
        Each line becomes a separate inference
        """

        # Split by newline and remove empty lines / trim spaces
        prompt_list = [line.strip() for line in prompts.split('\n') if line.strip()]

        if not prompt_list:
            print("[Prompt Batcher] ⚠️ No prompts provided, returning empty prompt")
            return ([""],)

        # Append style safely if provided, avoiding duplicates
        if style:
            prompt_list = [
                f"{p}, {style}" if style not in p else p
                for p in prompt_list
            ]

        # Debug: print each prompt for verification
        print(f"[Prompt Batcher] 📋 Batching {len(prompt_list)} prompts:")
        for i, prompt in enumerate(prompt_list, 1):
            preview = prompt[:60] + "..." if len(prompt) > 60 else prompt
            print(f"[Prompt Batcher]   {i}. {preview}")

        # Return as tuple containing the list (required by ComfyUI)
        return (prompt_list,)


NODE_CLASS_MAPPINGS = {
    "SimplePromptBatcher": SimplePromptBatcher
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimplePromptBatcher": "📝 Simple Prompt Batcher"
}

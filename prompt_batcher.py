"""
ComfyUI Simple Prompt Batcher
Takes multiple prompts (one per line) and outputs them one at a time for batch processing
"""

class SimplePromptBatcher:
    """
    Simple prompt batcher - one prompt per line
    Automatically batches through all prompts for inference
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Enter prompts here\nOne prompt per line\nNo empty lines between prompts"
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "batch_prompts"
    CATEGORY = "utils/text"
    OUTPUT_IS_LIST = (True,)  # This makes it output as a batch

    def batch_prompts(self, prompts):
        """
        Split prompts by newline and return as batch
        Each line becomes a separate inference
        """

        # Split by newlines and filter out empty lines
        prompt_list = [line.strip() for line in prompts.split('\n') if line.strip()]

        if not prompt_list:
            print("[Prompt Batcher] ⚠️ No prompts provided, returning empty prompt")
            return ([""],)

        print(f"[Prompt Batcher] 📋 Batching {len(prompt_list)} prompts:")
        for i, prompt in enumerate(prompt_list, 1):
            preview = prompt[:60] + "..." if len(prompt) > 60 else prompt
            print(f"[Prompt Batcher]   {i}. {preview}")

        # Return as tuple containing list (required by ComfyUI)
        return (prompt_list,)


NODE_CLASS_MAPPINGS = {
    "SimplePromptBatcher": SimplePromptBatcher
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimplePromptBatcher": "📝 Simple Prompt Batcher"
}

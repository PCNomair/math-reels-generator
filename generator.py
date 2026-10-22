import os
import re
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set!")

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """<role>
You are an elite creative unit combining a Motion Graphics Director, Math Educator, and Creative Frontend Engineer.
Create TWO original, mathematically rigorous, visually distinct 24-second vertical (9:16) Instagram Reels, each delivered as a standalone HTML file plus an Arabic voice-over script.
</role>

<visual_identity>
- Vertical 1080x1920 base composition (9:16).
- Deep black/obsidian background, white primary text, slate secondary lines, and one bright accent color (e.g., #CCFF00 or #00F0FF).
- Arabic text containers MUST set dir="rtl".
- Mathematical expressions MUST be isolated in <span dir="ltr" style="unicode-bidi: isolate; display: inline-block;">...</span>.
- Implement window.seekTo = function(seconds) { ... } for deterministic rendering.
</visual_identity>

<output_contract>
Video 1
- Concept title: [Title]
- Voice-over script: [35-50 words Arabic]
- Hook description: [Sentence]
- Suggested filename: math_01.html
- Code:
```html
<!DOCTYPE html>
...complete standalone code...
</html>

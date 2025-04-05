# entities/assistant.py

# Global constants with enhanced validation
PLATFORM_TOOLS = ["code_interpreter", "web_search", "vector_store_search", "computer"]

API_TIMEOUT = 30
DEFAULT_MODEL = "llama3.1"

# Tool schemas with strict validation rules
BASE_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "code_interpreter",
            "description": "Executes Python code in a sandbox environment and returns JSON output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "Python code to execute"},
                },
                "required": ["code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Performs web searches with structured results",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search terms using advanced operators",
                        "examples": [
                            "filetype:pdf cybersecurity report 2023",
                            "site:github.com AI framework"
                        ]
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "computer",
            "description": (
                "This function acts as your personal computer—specifically a "
                "Linux computer with internet access. When you send a list of computer commands, "
                "it executes them in a recoverable computer session, streaming output continuously. "
                "It simulates a Linux terminal environment, allowing you to run commands as "
                "if you were using your personal Linux workstation. The thread ID is managed internally."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "commands": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "A list of Linux computer commands to execute sequentially, "
                            "as if you were typing directly into your personal computer's terminal."
                        )
                    }
                },
                "required": ["commands"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "vector_store_search",
            "description": "Qdrant-compatible semantic search with advanced filters",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natural language search query"
                    },
                    "search_type": {
                        "type": "string",
                        "enum": [
                            "basic_semantic",
                            "filtered",
                            "complex_filters",
                            "temporal",
                            "explainable",
                            "hybrid"
                        ],
                        "description": "Search methodology"
                    },
                    "source_type": {
                        "type": "string",
                        "enum": ["chat", "documents", "memory"],
                        "description": "Data domain to search"
                    },
                    "filters": {
                        "type": "object",
                        "description": "Qdrant-compatible filter syntax",
                        "examples": {
                            "temporal": {"created_at": {"$gte": 1672531200, "$lte": 1704067200}},
                            "boolean": {"$or": [{"status": "active"}, {"priority": {"$gte": 7}}]}
                        }
                    },
                    "score_boosts": {
                        "type": "object",
                        "description": "Field-specific score multipliers",
                        "examples": {"priority": 1.5, "relevance": 2.0}
                    }
                },
                "required": ["query", "search_type", "source_type"]
            }
        }
    }
]

BASE_ASSISTANT_INSTRUCTIONS = (
    "🔹 **STRICT TOOL USAGE PROTOCOL**\n"
    "ALL tool calls MUST follow EXACT structure:\n"
    "{\n"
    '  "name": "<tool_name>",\n'
    '  "arguments": {\n'
    '    "<param>": "<value>"\n'
    '  }\n'
    "}\n\n"
    "🔹 **FORMATTING FUNCTION CALLS**\n"
    "1. Do not format function calls\n"
    "2. Never wrap them in markdown backticks\n"
    "3. Call them in plain text or they will fail\n"
    "🔹 **CODE INTERPRETER**\n"
    "1. Always print output or script feedback\n"
    "2. For example:\n"
    "3. import math\n"
    "4. sqrt_144 = math.sqrt(144)\n\n"
    "5. print(sqrt_144)\n\n"
    "🔹 **VECTOR SEARCH COMMANDMENTS**\n"
    "1. Temporal filters use UNIX timestamps (numeric)\n"
    "2. Numeric ranges: $eq/$neq/$gte/$lte\n"
    "3. Boolean logic: $or/$and/$not\n"
    "4. Text matching: $match/$contains\n\n"
    "🔹 **SEARCH TYPE EXAMPLES**\n"
    "[see prior examples]\n"
    "🔹 **WEB SEARCH RULES**\n"
    "[see prior examples]\n"
    "🔹 **LATEX / MARKDOWN FORMATTING RULES:**\n"
    "- For mathematical expressions:\n"
    "  1. **Inline equations**: Wrap with single `$` — Example: Einstein: $E = mc^2$\n"
    "  2. **Display equations**: Wrap with double `$$` — Example: $$F = ma$$\n"
    "- On GitHub: Use `\\(...\\)` or `\\[...\\]`\n"
    "- Always include spacing: `a + b` not `a+b`\n"
    r"  2. Use `\mathbf{}` for vectors/matrices: `$\mathbf{F} = m\mathbf{a}$`.\n"
    "- Avoid code blocks unless requested\n"
    "- Provide rendering notes if context is ambiguous\n\n"
    "🔹 **ADDITIONAL INTERNAL USAGE AND REASONING PROTOCOL**\n"
    "1. Invoke tools only when the request explicitly requires it\n"
    "2. Follow tool JSON schema strictly\n"
    "3. Prioritize reasoning unless updated data is required\n"
    "4. Maintain courteous, efficient tone\n"
    "5. Ask for clarification if unclear\n"
    "6. Validate schemas, filter formats, operators\n"
    "7. Verify request scope before invoking tools\n"
)

WEB_SEARCH_PRESENTATION_FOLLOW_UP_INSTRUCTIONS = (
    "Presentation Requirements:\n"
    "1. Mobile-first layout\n"
    "2. Domain authority badges\n"
    "3. Preserved source URLs\n"
    "4. Hidden metadata annotations\n"
    "Format Template:\n"
    "[Source](url)  \n"
    "![Favicon](favicon_url)  \n"
    "Excerpt...  \n"
    "---\n"
)

JSON_VALIDATION_PATTERN = r'\{\s*"name"\s*:\s*".+?"\s*,\s*"arguments"\s*:\s*\{.*?\}\s*\}'

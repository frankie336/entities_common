# ------------------------------------------------
# Vendors sometimes have clashing model names.
# This can interfere with routing logic
# This map resolves any likely clashes
# Also serves as source of truth, describing
# supported models
# _________________________________________________

# ------------------------------------------------
# PROVIDER-SPECIFIC MODEL MAPS
# Each dictionary acts as the "driver" for that vendor
# _________________________________________________

DEEPSEEK_NATIVE_MODELS = {
    "deepseek-ai/deepseek-reasoner": "deepseek-reasoner",
    "deepseek-ai/deepseek-chat": "deepseek-chat",
}

TOGETHER_AI_MODELS = {
    # --- DeepSeek ---
    "together-ai/deepseek-ai/DeepSeek-R1": "deepseek-ai/DeepSeek-R1",
    "together-ai/deepseek-ai/DeepSeek-V3": "deepseek-ai/DeepSeek-V3",
    "together-ai/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    "together-ai/deepseek-ai/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B": "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    "together-ai/deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    # --- Meta Llama ---
    "together-ai/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8": "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    "together-ai/meta-llama/Llama-4-Scout-17B-16E-Instruct": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
    "together-ai/meta-llama/Llama-3.3-70B-Instruct-Turbo": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "together-ai/meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo": "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    "together-ai/meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo": "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    "together-ai/meta-llama/Llama-Vision-Free": "meta-llama/Llama-Vision-Free",
    "together-ai/meta-llama/LlamaGuard-2-8b": "meta-llama/LlamaGuard-2-8b",
    # --- Google ---
    "together-ai/google/gemma-2-9b-it": "google/gemma-2-9b-it",
    # --- Mistral ---
    "together-ai/mistralai/Mistral-7B-Instruct-v0.2": "mistralai/Mistral-7B-Instruct-v0.2",
    "together-ai/mistralai/Mistral-7B-Instruct-v0.3": "mistralai/Mistral-7B-Instruct-v0.3",
    # --- Qwen (Legacy/Existing) ---
    "together-ai/Qwen/QwQ-32B": "Qwen/QwQ-32B",
    "together-ai/Qwen/Qwen2.5-Coder-32B-Instruct": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "together-ai/Qwen/Qwen2-VL-72B-Instruct": "Qwen/Qwen2-VL-72B-Instruct",
    # --- Qwen (New Additions) ---
    # Qwen 3 Series
    "together-ai/Qwen/Qwen3-Next-80B-A3B-Instruct": "Qwen/Qwen3-Next-80B-A3B-Instruct",
    "together-ai/Qwen/Qwen3-Next-80B-A3B-Thinking": "Qwen/Qwen3-Next-80B-A3B-Thinking",
    "together-ai/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8": "Qwen/Qwen3-Next-80B-A3B-Instruct-FP8",
    "together-ai/Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8": "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
    "together-ai/Qwen/Qwen3-235B-A22B-Instruct-2507-tput": "Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
    "together-ai/Qwen/Qwen3-235B-A22B-fp8-tput": "Qwen/Qwen3-235B-A22B-fp8-tput",
    "together-ai/Qwen/Qwen3-235B-A22B-Thinking-2507": "Qwen/Qwen3-235B-A22B-Thinking-2507",
    "together-ai/Qwen/Qwen3-VL-8B-Instruct": "Qwen/Qwen3-VL-8B-Instruct",
    "together-ai/Qwen/Qwen3-VL-32B-Instruct": "Qwen/Qwen3-VL-32B-Instruct",
    "together-ai/Qwen/Qwen3-VL-235B-A22B-Instruct-FP": "Qwen/Qwen3-VL-235B-A22B-Instruct-FP",
    "together-ai/Qwen/Qwen3-8B": "Qwen/Qwen3-8B",
    "together-ai/Qwen/Qwen3-14B-Base": "Qwen/Qwen3-14B-Base",
    # Qwen 2.5 Series
    "together-ai/Qwen/Qwen2.5-72B-Instruct": "Qwen/Qwen2.5-72B-Instruct",
    "together-ai/Qwen/Qwen2.5-72B-Instruct-Turbo": "Qwen/Qwen2.5-72B-Instruct-Turbo",
    "together-ai/Qwen/Qwen2.5-VL-72B-Instruct": "Qwen/Qwen2.5-VL-72B-Instruct",
    "together-ai/Qwen/Qwen2.5-7B-Instruct-Turbo": "Qwen/Qwen2.5-7B-Instruct-Turbo",
    "together-ai/Qwen/Qwen2.5-1.5B": "Qwen/Qwen2.5-1.5B",
    # Misc
    "together-ai/Qwen/Qwen-Image": "Qwen/Qwen-Image",
    "together-ai/Qwen/Qwen2-7B": "Qwen/Qwen2-7B",
    # OpenAI
    "together-ai/openai/gpt-oss-120b": "openai/gpt-oss-120b",
    "together-ai/openai/gpt-oss-20b": "openai/gpt-oss-20b",
}


HYPERBOLIC_MODELS = {
    # DeepSeek
    "hyperbolic/deepseek-ai/DeepSeek-V3-0324": "deepseek-ai/DeepSeek-V3-0324",
    # new
    "hyperbolic/deepseek-ai/DeepSeek-R1-0528": "deepseek-ai/DeepSeek-R1-0528",
    "hyperbolic/deepseek-ai/DeepSeek-R1": "deepseek-ai/DeepSeek-R1",
    "hyperbolic/deepseek-ai/DeepSeek-V3": "deepseek-ai/DeepSeek-V3",
    # llama
    "hyperbolic/meta-llama/Llama-3.3-70B-Instruct": "meta-llama/Llama-3.3-70B-Instruct",
    "hyperbolic/meta-llama/Llama-3.2-3B-Instruct": "meta-llama/Llama-3.2-3B-Instruct",
    "hyperbolic/meta-llama/Meta-Llama-3.1-405B-Instruct": "meta-llama/Meta-Llama-3.1-405B-Instruct",
    "hyperbolic/meta-llama/Meta-Llama-3.1-8B-Instruct": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "hyperbolic/meta-llama/Meta-Llama-3.1-70B-Instruct": "meta-llama/Meta-Llama-3.1-70B-Instruct",
    "hyperbolic/meta-llama/Meta-Llama-3-70B-Instruct": "meta-llama/Meta-Llama-3-70B-Instruct",
    # Quen
    "hyperbolic/Qwen/QwQ-32B": "Qwen/QwQ-32B",
    "hyperbolic/Qwen/Qwen2.5-VL-7B-Instruct": "Qwen/Qwen2.5-VL-7B-Instruct",
    "hyperbolic/Qwen/Qwen2.5-Coder-32B-Instruct": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "hyperbolic/Qwen/Qwen2.5-72B-Instruct": "Qwen/Qwen2.5-72B-Instruct",
    "hyperbolic/Qwen/Qwen3-Next-80B-A3B-Thinking": "Qwen/Qwen3-Next-80B-A3B-Thinking",
    "hyperbolic/Qwen/Qwen3-Coder-480B-A35B-Instruct": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
    "hyperbolic/Qwen/Qwen3-235B-A22B-Instruct-2507": "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "hyperbolic/Qwen/Qwen3-235B-A22B": "Qwen/Qwen3-235B-A22B",
    # OpenAI
    "hyperbolic/openai/gpt-oss-120b": "openai/gpt-oss-120b",
    "hyperbolic/openai/gpt-oss-20b": "openai/gpt-oss-20b",
    # New
    "hyperbolic/openai/gpt-oss-120b-turbo": "openai/gpt-oss-120b-turbo",
}


# --- MASTER COMBINED MAP ---
# This merges them all into one flat lookup for the Router
MODEL_MAP = {
    **DEEPSEEK_NATIVE_MODELS,
    **TOGETHER_AI_MODELS,
    **HYPERBOLIC_MODELS,
}

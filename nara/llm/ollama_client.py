import subprocess
from nara.llm.prompt_registry import register
from nara.llm.model_selector import choose
from nara.llm.prompt_lock import lock

def call_llm(prompt: str, name="default") -> str:
    meta = register(name, prompt)
    lock(name, meta["hash"])

    model = choose(name)

    proc = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,  # IMPORTANT
    )

    return proc.stdout.decode("utf-8", errors="replace").strip()

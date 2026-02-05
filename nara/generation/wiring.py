def wire_components(components: list[dict]) -> dict:
    wiring = {}
    for i in range(len(components) - 1):
        wiring[components[i]["name"]] = components[i + 1]["name"]
    return wiring

class Print:
    def __init__(self):
        pass

    def debug_print(self, message) -> None:
        debug_message = f"[DEBUG] {message}"
        # ANSI escape code for green text
        print(f"\033[92m{debug_message}\033[0m")

    def debug_server_print(self, message) -> None:
        debug_message = f"[SERVER] {message}"
        # ANSI escape code for cyan text
        print(f"\033[96m{debug_message}\033[0m")

class PlayerException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] PLAYER: Player failure."
    if message:
        self.message = f"[ERROR] PLAYER: {message}\n{self.message}"
    super().__init__(self.message)
class CardException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] CARD: card failure."
    if message:
        self.message = f"[ERROR] CARD: {message}\n{self.message}"
    super().__init__(self.message)
class PawnException(Exception):
    
  def __init__(self, message = None):
    self.message = "[ERROR] PAWN: Pawn failure."
    if message:
        self.message = f"[ERROR] PAWN: {message}\n{self.message}"
    super().__init__(self.message)
    
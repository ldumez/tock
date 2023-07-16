class TeamException(Exception):

  def __init__(self, message = None):
    self.message = "[ERROR] TEAM: Team failure."
    if message:
        self.message = f"[ERROR] TEAM: {message}\n{self.message}"
    super().__init__(self.message)
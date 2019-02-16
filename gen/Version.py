class Version:
	def __init__(self, versionString: str):
		self.parts = versionString.split('.')
	
	def __str__(self):
		return '.'.join(self.parts)
	
	def toString(self, length: int) -> str:
		parts = self.parts.copy()
		while len(parts) > length and parts[-1] == '0':
			parts.pop()
		if len(parts) < length:
			parts += ['0'] * (length - len(parts))
		return '.'.join(parts)
	
	def String(self) -> str:
		return '.'.join(self.parts)

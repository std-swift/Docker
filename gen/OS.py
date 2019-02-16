from Version import Version

class OS:
	def __init__(self, version: str, name: str, codename: str):
		self.version = Version(version)
		self.name = name
		self.codename = codename
	
	def InstallCommand(self, dependency) -> str:
		raise NotImplementedError
	
	def UninstallCommand(self, dependency) -> str:
		raise NotImplementedError
	
	def DockerCleanup(self) -> str:
		raise NotImplementedError
	
	def DockerRUN(self, command: str) -> str:
		return '\tRUN {} >/dev/null\n'.format(command)
	
	def DockerInstall(self, dependencies: list) -> str:
		commands = ''
		for dependency in dependencies:
			commands += self.DockerRUN(self.InstallCommand(dependency))
		return commands
	
	def DockerUnintall(self, dependencies: list) -> str:
		commands = ''
		for dependency in dependencies:
			commands += self.DockerRUN(self.UninstallCommand(dependency))
		return commands
	
	def OSTags(self) -> list:
		return [
			self.name + self.version.toString(2).replace('.', ''),
			self.codename,
		]

class Ubuntu(OS):
	def __init__(self, version: str, codename: str):
		super().__init__(version, 'ubuntu', codename)
	
	def InstallCommand(self, dependency) -> str:
		return '$APT install {}'.format(dependency)
	
	def UninstallCommand(self, dependency) -> str:
		return '$APT remove {}'.format(dependency)
	
	def DockerCleanup(self) -> str:
		commands = ''
		commands += self.DockerRUN('$APT autoremove')
		commands += self.DockerRUN('$APT clean')
		commands += self.DockerRUN('rm -rf /var/lib/apt/lists/*')
		commands += self.DockerRUN('rm -rf /tmp/*')
		return commands


Ubuntu1404 = Ubuntu('14.04', 'trusty')
Ubuntu1604 = Ubuntu('16.04', 'xenial')
Ubuntu1804 = Ubuntu('18.04', 'bionic')

All = [
	Ubuntu1404,
	Ubuntu1604,
	Ubuntu1804,
]

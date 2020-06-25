import OS
import Swift
import itertools

class Combination:
	def __init__(self, os: OS.OS, swift: Swift.Swift, extraTags: list,
	                   keyDeps: list, buildDeps: list, deployDeps: list):
		self.os = os
		self.swift = swift
		self.extraTags = extraTags
		self.keyDependencies = keyDeps
		self.buildDependencies = buildDeps
		self.deployDependencies = deployDeps
		self.targets = ['Build', 'Deploy']
	
	def DockerBuildCommands(self) -> str:
		commands = '\tdocker build .\n'
		for target in self.targets:
			commands += '\tdocker build --target Swift{0} --tag {1} .\n' \
				.format(target, self.GetDevTag(target))
		return commands
	
	def DockerSquashCommands(self) -> str:
		commands = ''
		for target in self.targets:
			commands += '\tdocker-squash -t {0} {1}\n' \
				.format(self.GetSquashTag(target), self.GetDevTag(target))
		return commands
	
	def DockerTagCommands(self) -> str:
		_os = self.os.OSTags()
		_swift = self.swift.swiftTags + self.extraTags
		_targets = self.targets
		commands = ''
		for (os, swift, target) in itertools.product(_os, _swift, _targets):
			commands += '\tdocker tag {0} stdswift/{1}:{2}-{3}\n' \
				.format(
					self.GetSquashTag(target),
					target.lower(),
					os,
					swift,
				)
		return commands
	
	def DockerPushCommands(self) -> str:
		_os = self.os.OSTags()
		_swift = self.swift.swiftTags + self.extraTags
		_targets = self.targets
		commands = ''
		for (os, swift, target) in itertools.product(_os, _swift, _targets):
			commands += '\tdocker push stdswift/{0}:{1}-{2}\n' \
				.format(
					target.lower(),
					os,
					swift,
				)
		return commands
	
	def GetDevTag(self, target: str) -> str:
		return '{0}{1}-{2}-{3}-dev'.format(
			self.os.name,
			self.os.version.String(),
			self.swift.version.toString(3),
			target.lower(),
		)

	def GetSquashTag(self, target: str) -> str:
		return '{0}{1}-{2}-{3}-squash'.format(
			self.os.name,
			self.os.version.String(),
			self.swift.version.toString(3),
			target.lower(),
		)

kd1 = [
	'wget',
	'ca-certificates',
]
kd2 = kd1 + [
	'gnupg2'
]

bd1 = [
	'git',
	'clang',
	'binutils',
	'libicu-dev',
	'libxml2',
	'libcurl4-openssl-dev',
]
bd2 = bd1 + [
	'libbsd-dev'
]

dd1 = [
	'libatomic1',
]

Combinations = [
	Combination(OS.Ubuntu1404, Swift.Swift500, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift500, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift500, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift501, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift501, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift501, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift502, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift502, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift502, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift503, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift503, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift503, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift510, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift510, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift510, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift511, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift511, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift511, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift512, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift512, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift512, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift513, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift513, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift513, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift514, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift514, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift514, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1404, Swift.Swift515, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1604, Swift.Swift515, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift515, [], kd2, bd2, dd1),

	Combination(OS.Ubuntu1604, Swift.Swift520, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift520, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1604, Swift.Swift521, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift521, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1604, Swift.Swift522, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift522, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1604, Swift.Swift523, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift523, [], kd2, bd2, dd1),
	
	Combination(OS.Ubuntu1604, Swift.Swift524, [], kd1, bd1, dd1),
	Combination(OS.Ubuntu1804, Swift.Swift524, [], kd2, bd2, dd1),
	Combination(OS.Ubuntu2004, Swift.Swift524, [], kd2, bd2 + ['libedit-dev', 'libz3-4'], dd1),
]

from OS import OS
from Version import Version

class Swift:
	def __init__(self, version: str, swiftTags: list,
	                   suffix='release', flavor='RELEASE'):
		self.version = Version(version)
		self.swiftTags = [self.version.toString(3)] + swiftTags
		self.suffix = suffix
		self.flavor = flavor
	
	def Name(self) -> str:
		if self.flavor == 'RELEASE':
			return self.version.String()
		return self.version.String() + '-' + self.flavor
	
	def URL(self, os: OS) -> str:
		baseURL = 'https://swift.org/builds/swift-{3}-{4}/{0}{2}/swift-{3}-{5}/swift-{3}-{5}-{0}{1}.tar.gz'
		return baseURL.format(
			os.name,
			os.version.toString(2),
			os.version.toString(2).replace('.', ''),
			self.version.toString(2),
			self.suffix,
			self.flavor,
		)


Swift500 = Swift('5.0',   ['5.0', '5', 'latest'])

All = [
	Swift500,
]

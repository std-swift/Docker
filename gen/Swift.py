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


Swift500 = Swift('5.0',   [])
Swift501 = Swift('5.0.1', [])
Swift502 = Swift('5.0.2', [])
Swift503 = Swift('5.0.3', ['5.0'])
Swift510 = Swift('5.1',   [])
Swift511 = Swift('5.1.1', [])
Swift512 = Swift('5.1.2', [])
Swift513 = Swift('5.1.3', [])
Swift514 = Swift('5.1.4', [])
Swift515 = Swift('5.1.5', ['5.1'])
Swift520 = Swift('5.2',   [])
Swift521 = Swift('5.2.1', [])
Swift522 = Swift('5.2.2', [])
Swift523 = Swift('5.2.3', [])
Swift524 = Swift('5.2.4', ['5.2', '5', 'latest'])

All = [
	Swift500, Swift501, Swift502, Swift503,
	Swift510, Swift511, Swift512, Swift513, Swift514, Swift515,
	Swift520, Swift521, Swift522, Swift523, Swift524,
]

FROM ubuntu:14.04 AS Swift
	WORKDIR /tmp/
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	# Handle end of life
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update; \
		$APT install wget >/dev/null; \
		$APT install ca-certificates >/dev/null; \
		$APT autoremove; \
		$APT clean; \
		rm -rf /var/lib/apt/lists/*
	
	# Download Swift keys
	RUN mkdir -p -m 500 /tmp/gnupg
	RUN wget -q -O - https://swift.org/keys/all-keys.asc \
		| GNUPGHOME=/tmp/gnupg gpg --import -
	
	# Download Swift and check the signature
	RUN wget -q "https://swift.org/builds/swift-5.1.2-release/ubuntu1404/swift-5.1.2-RELEASE/swift-5.1.2-RELEASE-ubuntu14.04.tar.gz" -O swift.tar.gz
	RUN wget -q "https://swift.org/builds/swift-5.1.2-release/ubuntu1404/swift-5.1.2-RELEASE/swift-5.1.2-RELEASE-ubuntu14.04.tar.gz.sig" -O swift.tar.gz.sig
	RUN GNUPGHOME=/tmp/gnupg gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz
	RUN mkdir /swift && tar xzf swift.tar.gz --directory /swift --strip-components=1





FROM ubuntu:14.04 AS SwiftBuild
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update; \
		$APT install ca-certificates >/dev/null; \
		$APT install git >/dev/null; \
		$APT install clang >/dev/null; \
		$APT install binutils >/dev/null; \
		$APT install libicu-dev >/dev/null; \
		$APT install libxml2 >/dev/null; \
		$APT install libcurl4-openssl-dev >/dev/null; \
		$APT autoremove; \
		$APT clean; \
		rm -rf /var/lib/apt/lists/*
	COPY --from=Swift /swift /





FROM ubuntu:14.04 AS SwiftDeploy
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update; \
		$APT install libatomic1 >/dev/null; \
		$APT autoremove; \
		$APT clean; \
		rm -rf /var/lib/apt/lists/*
	COPY --from=SwiftBuild /usr/lib/swift/linux /usr/lib/swift/linux





FROM SwiftBuild AS TestBuild
	WORKDIR /tmp/
	RUN swift package init --type executable
	RUN swift build
	RUN swift test
	RUN swift run

FROM SwiftDeploy AS TestDeploy
	WORKDIR /tmp/
	COPY --from=TestBuild /tmp/.build/debug/tmp .
	RUN ./tmp

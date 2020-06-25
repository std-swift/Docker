FROM ubuntu:16.04 AS Base
	WORKDIR /tmp/
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	# Handle end of life
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update
	
	# Remove these later
	RUN $APT install wget >/dev/null
	RUN $APT install ca-certificates >/dev/null

	# Download Swift keys
	RUN mkdir -p -m 500 /tmp/gnupg
	RUN wget -q -O - https://swift.org/keys/all-keys.asc \
		| GNUPGHOME=/tmp/gnupg gpg --import -





FROM Base AS SwiftBuild
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT install git >/dev/null
	RUN $APT install clang >/dev/null
	RUN $APT install binutils >/dev/null
	RUN $APT install libicu-dev >/dev/null
	RUN $APT install libxml2 >/dev/null
	RUN $APT install libcurl4-openssl-dev >/dev/null

	RUN wget -q "https://swift.org/builds/swift-5.2.2-release/ubuntu1604/swift-5.2.2-RELEASE/swift-5.2.2-RELEASE-ubuntu16.04.tar.gz" -O swift.tar.gz
	RUN wget -q "https://swift.org/builds/swift-5.2.2-release/ubuntu1604/swift-5.2.2-RELEASE/swift-5.2.2-RELEASE-ubuntu16.04.tar.gz.sig" -O swift.tar.gz.sig
	RUN GNUPGHOME=/tmp/gnupg gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz
	RUN tar xzf swift.tar.gz --directory / --strip-components=1
	
	# Remove
	RUN $APT remove wget >/dev/null
	RUN $APT remove ca-certificates >/dev/null

	# Cleanup
	RUN $APT autoremove >/dev/null
	RUN $APT clean >/dev/null
	RUN rm -rf /var/lib/apt/lists/* >/dev/null
	RUN rm -rf /tmp/* >/dev/null






FROM Base AS SwiftDeploy
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT install libatomic1 >/dev/null

	COPY --from=SwiftBuild /usr/lib/swift/linux /usr/lib/swift/linux	
	
	# Remove
	RUN $APT remove wget >/dev/null
	RUN $APT remove ca-certificates >/dev/null

	# Cleanup
	RUN $APT autoremove >/dev/null
	RUN $APT clean >/dev/null
	RUN rm -rf /var/lib/apt/lists/* >/dev/null
	RUN rm -rf /tmp/* >/dev/null






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

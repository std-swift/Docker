FROM ubuntu:{OS.Version} AS Swift
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
{OS.Requirements.Key}		$APT autoremove; \
		$APT clean; \
		rm -rf /var/lib/apt/lists/*
	
	# Download Swift keys
	RUN mkdir -p -m 500 /tmp/gnupg
	RUN wget -q -O - https://swift.org/keys/all-keys.asc \
		| GNUPGHOME=/tmp/gnupg gpg --import -
	
	# Download Swift and check the signature
	RUN wget -q "{Swift.URL}" -O swift.tar.gz
	RUN wget -q "{Swift.URL}.sig" -O swift.tar.gz.sig
	RUN GNUPGHOME=/tmp/gnupg gpg --batch --verify --quiet swift.tar.gz.sig swift.tar.gz
	RUN mkdir /swift && tar xzf swift.tar.gz --directory /swift --strip-components=1





FROM ubuntu:{OS.Version} AS SwiftBuild
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update; \
{OS.Requirements.Build}		$APT autoremove; \
		$APT clean; \
		rm -rf /var/lib/apt/lists/*
	COPY --from=Swift /swift /





FROM ubuntu:{OS.Version} AS SwiftDeploy
	WORKDIR /
	ARG DEBIAN_FRONTEND=noninteractive
	ARG APT="apt-get -qq --no-install-recommends"
	
	RUN $APT update; \
		if [ $? -eq 100 ]; \
		then \
			sed -i -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list; \
		fi; \
		$APT update; \
{OS.Requirements.Deploy}		$APT autoremove; \
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

.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu20.04-5.2.4-build-dev .
	docker build --target SwiftDeploy --tag ubuntu20.04-5.2.4-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:ubuntu2004-5.2.4
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:ubuntu2004-5.2.4
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:ubuntu2004-5.2
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:ubuntu2004-5.2
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:ubuntu2004-5
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:ubuntu2004-5
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:ubuntu2004-latest
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:ubuntu2004-latest
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:focal-5.2.4
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:focal-5.2.4
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:focal-5.2
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:focal-5.2
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:focal-5
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:focal-5
	docker tag ubuntu20.04-5.2.4-build-dev stdswift/build:focal-latest
	docker tag ubuntu20.04-5.2.4-deploy-dev stdswift/deploy:focal-latest

	docker push stdswift/build:ubuntu2004-5.2.4
	docker push stdswift/deploy:ubuntu2004-5.2.4
	docker push stdswift/build:ubuntu2004-5.2
	docker push stdswift/deploy:ubuntu2004-5.2
	docker push stdswift/build:ubuntu2004-5
	docker push stdswift/deploy:ubuntu2004-5
	docker push stdswift/build:ubuntu2004-latest
	docker push stdswift/deploy:ubuntu2004-latest
	docker push stdswift/build:focal-5.2.4
	docker push stdswift/deploy:focal-5.2.4
	docker push stdswift/build:focal-5.2
	docker push stdswift/deploy:focal-5.2
	docker push stdswift/build:focal-5
	docker push stdswift/deploy:focal-5
	docker push stdswift/build:focal-latest
	docker push stdswift/deploy:focal-latest


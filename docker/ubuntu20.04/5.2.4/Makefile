.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu20.04-5.2.4-build-dev .
	docker build --target SwiftDeploy --tag ubuntu20.04-5.2.4-deploy-dev .

	docker-squash -t ubuntu20.04-5.2.4-build-squash ubuntu20.04-5.2.4-build-dev
	docker-squash -t ubuntu20.04-5.2.4-deploy-squash ubuntu20.04-5.2.4-deploy-dev

	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:ubuntu2004-5.2.4
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:ubuntu2004-5.2.4
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:ubuntu2004-5.2
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:ubuntu2004-5.2
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:ubuntu2004-5
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:ubuntu2004-5
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:ubuntu2004-latest
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:ubuntu2004-latest
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:focal-5.2.4
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:focal-5.2.4
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:focal-5.2
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:focal-5.2
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:focal-5
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:focal-5
	docker tag ubuntu20.04-5.2.4-build-squash stdswift/build:focal-latest
	docker tag ubuntu20.04-5.2.4-deploy-squash stdswift/deploy:focal-latest


.PHONY: upload
upload:
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


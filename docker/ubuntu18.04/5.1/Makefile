.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.1.0-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.1.0-deploy-dev .

	docker-squash -t ubuntu18.04-5.1.0-build-squash ubuntu18.04-5.1.0-build-dev
	docker-squash -t ubuntu18.04-5.1.0-deploy-squash ubuntu18.04-5.1.0-deploy-dev

	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:ubuntu1804-5.1.0
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:ubuntu1804-5.1.0
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:ubuntu1804-5.1
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:ubuntu1804-5.1
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:ubuntu1804-5
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:ubuntu1804-5
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:ubuntu1804-latest
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:ubuntu1804-latest
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:bionic-5.1.0
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:bionic-5.1.0
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:bionic-5.1
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:bionic-5.1
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:bionic-5
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:bionic-5
	docker tag ubuntu18.04-5.1.0-build-squash stdswift/build:bionic-latest
	docker tag ubuntu18.04-5.1.0-deploy-squash stdswift/deploy:bionic-latest


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1804-5.1.0
	docker push stdswift/deploy:ubuntu1804-5.1.0
	docker push stdswift/build:ubuntu1804-5.1
	docker push stdswift/deploy:ubuntu1804-5.1
	docker push stdswift/build:ubuntu1804-5
	docker push stdswift/deploy:ubuntu1804-5
	docker push stdswift/build:ubuntu1804-latest
	docker push stdswift/deploy:ubuntu1804-latest
	docker push stdswift/build:bionic-5.1.0
	docker push stdswift/deploy:bionic-5.1.0
	docker push stdswift/build:bionic-5.1
	docker push stdswift/deploy:bionic-5.1
	docker push stdswift/build:bionic-5
	docker push stdswift/deploy:bionic-5
	docker push stdswift/build:bionic-latest
	docker push stdswift/deploy:bionic-latest


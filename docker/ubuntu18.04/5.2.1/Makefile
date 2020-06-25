.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.2.1-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.2.1-deploy-dev .

	docker-squash -t ubuntu18.04-5.2.1-build-squash ubuntu18.04-5.2.1-build-dev
	docker-squash -t ubuntu18.04-5.2.1-deploy-squash ubuntu18.04-5.2.1-deploy-dev

	docker tag ubuntu18.04-5.2.1-build-squash stdswift/build:ubuntu1804-5.2.1
	docker tag ubuntu18.04-5.2.1-deploy-squash stdswift/deploy:ubuntu1804-5.2.1
	docker tag ubuntu18.04-5.2.1-build-squash stdswift/build:bionic-5.2.1
	docker tag ubuntu18.04-5.2.1-deploy-squash stdswift/deploy:bionic-5.2.1


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1804-5.2.1
	docker push stdswift/deploy:ubuntu1804-5.2.1
	docker push stdswift/build:bionic-5.2.1
	docker push stdswift/deploy:bionic-5.2.1


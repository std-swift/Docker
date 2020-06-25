.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.2.3-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.2.3-deploy-dev .

	docker-squash -t ubuntu18.04-5.2.3-build-squash ubuntu18.04-5.2.3-build-dev
	docker-squash -t ubuntu18.04-5.2.3-deploy-squash ubuntu18.04-5.2.3-deploy-dev

	docker tag ubuntu18.04-5.2.3-build-squash stdswift/build:ubuntu1804-5.2.3
	docker tag ubuntu18.04-5.2.3-deploy-squash stdswift/deploy:ubuntu1804-5.2.3
	docker tag ubuntu18.04-5.2.3-build-squash stdswift/build:bionic-5.2.3
	docker tag ubuntu18.04-5.2.3-deploy-squash stdswift/deploy:bionic-5.2.3


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1804-5.2.3
	docker push stdswift/deploy:ubuntu1804-5.2.3
	docker push stdswift/build:bionic-5.2.3
	docker push stdswift/deploy:bionic-5.2.3


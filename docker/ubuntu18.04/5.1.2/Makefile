.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.1.2-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.1.2-deploy-dev .

	docker-squash -t ubuntu18.04-5.1.2-build-squash ubuntu18.04-5.1.2-build-dev
	docker-squash -t ubuntu18.04-5.1.2-deploy-squash ubuntu18.04-5.1.2-deploy-dev

	docker tag ubuntu18.04-5.1.2-build-squash stdswift/build:ubuntu1804-5.1.2
	docker tag ubuntu18.04-5.1.2-deploy-squash stdswift/deploy:ubuntu1804-5.1.2
	docker tag ubuntu18.04-5.1.2-build-squash stdswift/build:bionic-5.1.2
	docker tag ubuntu18.04-5.1.2-deploy-squash stdswift/deploy:bionic-5.1.2


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1804-5.1.2
	docker push stdswift/deploy:ubuntu1804-5.1.2
	docker push stdswift/build:bionic-5.1.2
	docker push stdswift/deploy:bionic-5.1.2


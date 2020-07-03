.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.0.0-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.0.0-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu18.04-5.0.0-build-dev stdswift/build:ubuntu1804-5.0.0
	docker tag ubuntu18.04-5.0.0-deploy-dev stdswift/deploy:ubuntu1804-5.0.0
	docker tag ubuntu18.04-5.0.0-build-dev stdswift/build:bionic-5.0.0
	docker tag ubuntu18.04-5.0.0-deploy-dev stdswift/deploy:bionic-5.0.0

	docker push stdswift/build:ubuntu1804-5.0.0
	docker push stdswift/deploy:ubuntu1804-5.0.0
	docker push stdswift/build:bionic-5.0.0
	docker push stdswift/deploy:bionic-5.0.0


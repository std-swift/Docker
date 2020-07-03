.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu18.04-5.2.4-build-dev .
	docker build --target SwiftDeploy --tag ubuntu18.04-5.2.4-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:ubuntu1804-5.2.4
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1804-5.2.4
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:ubuntu1804-5.2
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1804-5.2
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:ubuntu1804-5
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1804-5
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:ubuntu1804-latest
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1804-latest
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:bionic-5.2.4
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:bionic-5.2.4
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:bionic-5.2
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:bionic-5.2
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:bionic-5
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:bionic-5
	docker tag ubuntu18.04-5.2.4-build-dev stdswift/build:bionic-latest
	docker tag ubuntu18.04-5.2.4-deploy-dev stdswift/deploy:bionic-latest

	docker push stdswift/build:ubuntu1804-5.2.4
	docker push stdswift/deploy:ubuntu1804-5.2.4
	docker push stdswift/build:ubuntu1804-5.2
	docker push stdswift/deploy:ubuntu1804-5.2
	docker push stdswift/build:ubuntu1804-5
	docker push stdswift/deploy:ubuntu1804-5
	docker push stdswift/build:ubuntu1804-latest
	docker push stdswift/deploy:ubuntu1804-latest
	docker push stdswift/build:bionic-5.2.4
	docker push stdswift/deploy:bionic-5.2.4
	docker push stdswift/build:bionic-5.2
	docker push stdswift/deploy:bionic-5.2
	docker push stdswift/build:bionic-5
	docker push stdswift/deploy:bionic-5
	docker push stdswift/build:bionic-latest
	docker push stdswift/deploy:bionic-latest


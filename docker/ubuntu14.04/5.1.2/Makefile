.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu14.04-5.1.2-build-dev .
	docker build --target SwiftDeploy --tag ubuntu14.04-5.1.2-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu14.04-5.1.2-build-dev stdswift/build:ubuntu1404-5.1.2
	docker tag ubuntu14.04-5.1.2-deploy-dev stdswift/deploy:ubuntu1404-5.1.2
	docker tag ubuntu14.04-5.1.2-build-dev stdswift/build:trusty-5.1.2
	docker tag ubuntu14.04-5.1.2-deploy-dev stdswift/deploy:trusty-5.1.2

	docker push stdswift/build:ubuntu1404-5.1.2
	docker push stdswift/deploy:ubuntu1404-5.1.2
	docker push stdswift/build:trusty-5.1.2
	docker push stdswift/deploy:trusty-5.1.2


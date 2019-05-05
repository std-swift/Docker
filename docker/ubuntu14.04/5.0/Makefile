.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu14.04-5.0.0-build-dev .
	docker build --target SwiftDeploy --tag ubuntu14.04-5.0.0-deploy-dev .

	docker-squash -t ubuntu14.04-5.0.0-build-squash ubuntu14.04-5.0.0-build-dev
	docker-squash -t ubuntu14.04-5.0.0-deploy-squash ubuntu14.04-5.0.0-deploy-dev

	docker tag ubuntu14.04-5.0.0-build-squash stdswift/build:ubuntu1404-5.0.0
	docker tag ubuntu14.04-5.0.0-deploy-squash stdswift/deploy:ubuntu1404-5.0.0
	docker tag ubuntu14.04-5.0.0-build-squash stdswift/build:trusty-5.0.0
	docker tag ubuntu14.04-5.0.0-deploy-squash stdswift/deploy:trusty-5.0.0


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1404-5.0.0
	docker push stdswift/deploy:ubuntu1404-5.0.0
	docker push stdswift/build:trusty-5.0.0
	docker push stdswift/deploy:trusty-5.0.0


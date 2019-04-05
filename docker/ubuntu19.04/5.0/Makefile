.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu19.04-5.0.0-build-dev .
	docker build --target SwiftDeploy --tag ubuntu19.04-5.0.0-deploy-dev .

	docker-squash -t ubuntu19.04-5.0.0-build-squash ubuntu19.04-5.0.0-build-dev
	docker-squash -t ubuntu19.04-5.0.0-deploy-squash ubuntu19.04-5.0.0-deploy-dev

	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:ubuntu1904-5.0.0
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:ubuntu1904-5.0.0
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:ubuntu1904-5.0
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:ubuntu1904-5.0
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:ubuntu1904-5
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:ubuntu1904-5
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:ubuntu1904-latest
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:ubuntu1904-latest
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:disco-5.0.0
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:disco-5.0.0
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:disco-5.0
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:disco-5.0
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:disco-5
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:disco-5
	docker tag ubuntu19.04-5.0.0-build-squash stdswift/build:disco-latest
	docker tag ubuntu19.04-5.0.0-deploy-squash stdswift/deploy:disco-latest


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1904-5.0.0
	docker push stdswift/deploy:ubuntu1904-5.0.0
	docker push stdswift/build:ubuntu1904-5.0
	docker push stdswift/deploy:ubuntu1904-5.0
	docker push stdswift/build:ubuntu1904-5
	docker push stdswift/deploy:ubuntu1904-5
	docker push stdswift/build:ubuntu1904-latest
	docker push stdswift/deploy:ubuntu1904-latest
	docker push stdswift/build:disco-5.0.0
	docker push stdswift/deploy:disco-5.0.0
	docker push stdswift/build:disco-5.0
	docker push stdswift/deploy:disco-5.0
	docker push stdswift/build:disco-5
	docker push stdswift/deploy:disco-5
	docker push stdswift/build:disco-latest
	docker push stdswift/deploy:disco-latest


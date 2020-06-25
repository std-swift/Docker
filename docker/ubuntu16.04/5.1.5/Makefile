.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu16.04-5.1.5-build-dev .
	docker build --target SwiftDeploy --tag ubuntu16.04-5.1.5-deploy-dev .

	docker-squash -t ubuntu16.04-5.1.5-build-squash ubuntu16.04-5.1.5-build-dev
	docker-squash -t ubuntu16.04-5.1.5-deploy-squash ubuntu16.04-5.1.5-deploy-dev

	docker tag ubuntu16.04-5.1.5-build-squash stdswift/build:ubuntu1604-5.1.5
	docker tag ubuntu16.04-5.1.5-deploy-squash stdswift/deploy:ubuntu1604-5.1.5
	docker tag ubuntu16.04-5.1.5-build-squash stdswift/build:ubuntu1604-5.1
	docker tag ubuntu16.04-5.1.5-deploy-squash stdswift/deploy:ubuntu1604-5.1
	docker tag ubuntu16.04-5.1.5-build-squash stdswift/build:xenial-5.1.5
	docker tag ubuntu16.04-5.1.5-deploy-squash stdswift/deploy:xenial-5.1.5
	docker tag ubuntu16.04-5.1.5-build-squash stdswift/build:xenial-5.1
	docker tag ubuntu16.04-5.1.5-deploy-squash stdswift/deploy:xenial-5.1


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1604-5.1.5
	docker push stdswift/deploy:ubuntu1604-5.1.5
	docker push stdswift/build:ubuntu1604-5.1
	docker push stdswift/deploy:ubuntu1604-5.1
	docker push stdswift/build:xenial-5.1.5
	docker push stdswift/deploy:xenial-5.1.5
	docker push stdswift/build:xenial-5.1
	docker push stdswift/deploy:xenial-5.1


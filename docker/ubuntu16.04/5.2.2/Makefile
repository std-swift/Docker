.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu16.04-5.2.2-build-dev .
	docker build --target SwiftDeploy --tag ubuntu16.04-5.2.2-deploy-dev .

	docker-squash -t ubuntu16.04-5.2.2-build-squash ubuntu16.04-5.2.2-build-dev
	docker-squash -t ubuntu16.04-5.2.2-deploy-squash ubuntu16.04-5.2.2-deploy-dev

	docker tag ubuntu16.04-5.2.2-build-squash stdswift/build:ubuntu1604-5.2.2
	docker tag ubuntu16.04-5.2.2-deploy-squash stdswift/deploy:ubuntu1604-5.2.2
	docker tag ubuntu16.04-5.2.2-build-squash stdswift/build:xenial-5.2.2
	docker tag ubuntu16.04-5.2.2-deploy-squash stdswift/deploy:xenial-5.2.2


.PHONY: upload
upload:
	docker push stdswift/build:ubuntu1604-5.2.2
	docker push stdswift/deploy:ubuntu1604-5.2.2
	docker push stdswift/build:xenial-5.2.2
	docker push stdswift/deploy:xenial-5.2.2


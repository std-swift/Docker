.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu16.04-5.1.5-build-dev .
	docker build --target SwiftDeploy --tag ubuntu16.04-5.1.5-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu16.04-5.1.5-build-dev stdswift/build:ubuntu1604-5.1.5
	docker tag ubuntu16.04-5.1.5-deploy-dev stdswift/deploy:ubuntu1604-5.1.5
	docker tag ubuntu16.04-5.1.5-build-dev stdswift/build:ubuntu1604-5.1
	docker tag ubuntu16.04-5.1.5-deploy-dev stdswift/deploy:ubuntu1604-5.1
	docker tag ubuntu16.04-5.1.5-build-dev stdswift/build:xenial-5.1.5
	docker tag ubuntu16.04-5.1.5-deploy-dev stdswift/deploy:xenial-5.1.5
	docker tag ubuntu16.04-5.1.5-build-dev stdswift/build:xenial-5.1
	docker tag ubuntu16.04-5.1.5-deploy-dev stdswift/deploy:xenial-5.1

	docker push stdswift/build:ubuntu1604-5.1.5
	docker push stdswift/deploy:ubuntu1604-5.1.5
	docker push stdswift/build:ubuntu1604-5.1
	docker push stdswift/deploy:ubuntu1604-5.1
	docker push stdswift/build:xenial-5.1.5
	docker push stdswift/deploy:xenial-5.1.5
	docker push stdswift/build:xenial-5.1
	docker push stdswift/deploy:xenial-5.1


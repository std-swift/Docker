.PHONY: all
all:
	docker build .
	docker build --target SwiftBuild --tag ubuntu16.04-5.2.4-build-dev .
	docker build --target SwiftDeploy --tag ubuntu16.04-5.2.4-deploy-dev .


.PHONY: upload
upload:
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:ubuntu1604-5.2.4
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1604-5.2.4
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:ubuntu1604-5.2
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1604-5.2
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:ubuntu1604-5
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1604-5
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:ubuntu1604-latest
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:ubuntu1604-latest
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:xenial-5.2.4
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:xenial-5.2.4
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:xenial-5.2
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:xenial-5.2
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:xenial-5
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:xenial-5
	docker tag ubuntu16.04-5.2.4-build-dev stdswift/build:xenial-latest
	docker tag ubuntu16.04-5.2.4-deploy-dev stdswift/deploy:xenial-latest

	docker push stdswift/build:ubuntu1604-5.2.4
	docker push stdswift/deploy:ubuntu1604-5.2.4
	docker push stdswift/build:ubuntu1604-5.2
	docker push stdswift/deploy:ubuntu1604-5.2
	docker push stdswift/build:ubuntu1604-5
	docker push stdswift/deploy:ubuntu1604-5
	docker push stdswift/build:ubuntu1604-latest
	docker push stdswift/deploy:ubuntu1604-latest
	docker push stdswift/build:xenial-5.2.4
	docker push stdswift/deploy:xenial-5.2.4
	docker push stdswift/build:xenial-5.2
	docker push stdswift/deploy:xenial-5.2
	docker push stdswift/build:xenial-5
	docker push stdswift/deploy:xenial-5
	docker push stdswift/build:xenial-latest
	docker push stdswift/deploy:xenial-latest


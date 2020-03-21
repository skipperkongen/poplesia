hello:
	echo 'Hello World'
.PHONY: hello

docker_build:
	docker build -t poplesia .
.PHONY: docker_build

docker_run: docker_build
	docker run -p 127.0.0.1:80:8000 poplesia
.PHONY: docker_run

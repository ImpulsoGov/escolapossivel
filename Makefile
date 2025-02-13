IMAGE_TAG=impulsogov/escola

UNAME := $(shell uname)
ifeq ($(UNAME), Linux)
SHELL := /bin/bash
else
SHELL := /bin/sh
endif

###
# Docker
###

# Build image
docker-build:
	docker build -t $(IMAGE_TAG) .

# Run just like the production environment
docker-run:
	docker run -d \
		--restart=unless-stopped \
		--name escolasegura \
		-v $(PWD)/.env:/home/ubuntu/.env:ro \
		-p 8001:8001 \
		-p 5000:5000 \
		$(IMAGE_TAG)

# Run development server with file binding from './src'
start-redis:
	docker run --rm -d --name redis -p 6379:6379 redis:5
destroy-redis:
	docker rm -f redis

docker-remove:
	docker rm -f escolasegura 2>/dev/null || true

docker-dev: docker-remove
	touch $(PWD)/.env
	
	docker run --rm -it \
		--name escolasegura \
		-p 8001:8001 \
		-p 5000:5000 \
		-v $(PWD)/.env:/home/ubuntu/.env:ro \
		-v $(PWD)/src:/home/ubuntu/src:ro \
		$(IMAGE_TAG)

# Groups
docker-build-run: docker-build docker-run
docker-build-dev: docker-build docker-dev

# DEBUGING for production environment
docker-shell:
	docker run --rm -it \
		--entrypoint "/bin/bash" \
		-v $(PWD)/.env:/home/ubuntu/.env:ro \
		$(IMAGE_TAG)

# DEBUGING for staging environment
docker-heroku-test: docker-build
	docker run -it --rm \
		--name escolasegura \
		-e PORT=8080 \
		-p 8080:8080 \
		-p 5000:5000 \
		$(IMAGE_TAG)

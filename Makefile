PROJECT_NAME=fake-review-api
DOCKER_IMAGE=$(PROJECT_NAME)
DOCKER_TAG=dev
DOCKER_CONTAINER=$(PROJECT_NAME)-container

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run the container and mount the local code directory
run:
	docker run --rm -it \
		-p 8000:8000 \
		-v ${PWD}/app:/app/app \
		-v ${PWD}/model:/app/model \
		--name $(DOCKER_CONTAINER) \
		$(DOCKER_IMAGE):$(DOCKER_TAG)

# Stop the container (if running in detached mode)
stop:
	docker stop $(DOCKER_CONTAINER)

# Rebuild + rerun
reload: build run

# Run training script inside container (if needed)
train:
	docker run --rm -v ${PWD}:/app -w /app $(DOCKER_IMAGE):$(DOCKER_TAG) python train_dummy_model.py

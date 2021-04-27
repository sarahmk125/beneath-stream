build:
	@docker build -t beneath-stream .

run:
	@docker run --volume $(pwd):/beneath-stream -it beneath-stream

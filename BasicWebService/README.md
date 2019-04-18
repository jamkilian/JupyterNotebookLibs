### Commands to Start
```bash
# Build the container image (from inside this dir)
docker build -t flask_app .

# Run the container
docker run --name flask_app -d -p 8080:8080 flask_app
```
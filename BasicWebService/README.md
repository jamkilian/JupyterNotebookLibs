### Commands to Start
```bash
# Build the container image (from inside this dir)
docker build -t flask_app .

# Run the container
docker run --name flask_app -d -p 8080:8080 flask_app
```

### Creating Kubernetes Cluster
```bash
# Define kub yml config
cat ./deployment_flask_app.yml

# Create Deployment
kubectl create -f ./deployment_flask_app.yml

# Create Service definition
cat ./service_flask_app.yml
```
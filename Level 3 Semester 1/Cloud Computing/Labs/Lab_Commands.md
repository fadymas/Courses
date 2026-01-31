# 🐳 Docker and Kubernetes Cheatsheet

This cheatsheet summarizes essential Docker and Kubernetes commands for quick reference, grouped by function.
--
Created by Eng. Andrew Adel

---

## 💻 Core Docker CLIs

These are the most fundamental commands for interacting with Docker.

| Command | Description |
| :--- | :--- |
| `docker run [image]` | Run a command in a new container (= create + start) |
| `docker build` | Build an image from a Dockerfile |
| `docker push` | Push an image to a registry |
| `docker pull` | Pull an image from a registry |
| `docker stop [container]` | Gracefully stop a running container |
| `docker rm [container]` | Remove one or more containers |

---

## 🧰 Container Management

Commands for lifecycle management and listing of containers.

| Command | Description |
| :--- | :--- |
| `docker create [image]` | Create a container but do not start it |
| `docker start [container]` | Start a stopped container |
| `docker restart [container]` | Stop and then start a container |
| `docker kill [container]` | Kill the container (sends SIGKILL) |
| `docker pause [container]` | Suspend the container |
| `docker unpause [container]` | Resume the container |
| `docker wait [container]` | Block until one or more containers stop, then print their exit codes |
| `docker ps` | List **running** containers |
| `docker ps -a` | List **all** containers (running and stopped) |
| `docker logs [container]` | Show the container output (stdout + stderr) |
| `docker top [container]` | Display the running processes of a container |
| `docker diff [container]` | Show the differences with the image (modified files) |

---

## 🧑‍💻 Interacting with Containers

Commands for running commands inside or exchanging data with a container.

| Command | Description |
| :--- | :--- |
| `docker exec [container] [command]` | Run a command in an existing container (useful for debugging) |
| `docker cp [container]:[path] [hostpath]` | Copy files **from** the container to the host |
| `docker cp [hostpath] [container]:[path]` | Copy files **into** the container from the host |
| `docker export [container]` | Export the content of the container (tar archive) |
| `docker commit [container] [image]` | Commit a new docker image (snapshot of the container's changes) |

---

## 🏗️ Image Management

Commands for viewing, tagging and cleaning up local images.

| Command | Description |
| :--- | :--- |
| `docker images` | List all local images |
| `docker rmi [image]` | Delete one or more images |
| `docker history [image]` | Show the image history (list of ancestors) |
| `docker inspect [image]` | Show info's (in JSON format) |

---

## ⚡ Dockerfile Instructions

| Instruction | Description |
| :--- | :--- |
| `FROM` | Base image |
| `LABEL` | Adds metadata to an image |
| `RUN` | Execute commands in a new layer and commit the results |
| `ADD / COPY` | Adds files and folders into the image |
| `CMD` | Default command run on container start |
| `ENTRYPOINT` | Configures a container to run as an executable |
| `VOLUME` | Creates a mount point for external volumes |
| `EXPOSE` | Informs the container which port to listen on |
| `ENV` | Sets environment variables |
| `USER` | Sets the user name or UID |
| `WORKDIR` | Sets the working directory |
| `ARG` | Defines a build-time variable |
| `ONBUILD` | Adds a trigger instruction executed later |

---

## 🧩 Docker Compose Commands

| Command | Description |
| :--- | :--- |
| `docker compose up` | Start all services |
| `docker compose up -d` | Start in detached mode |
| `docker compose down` | Stop and remove containers, networks |
| `docker compose ps` | List containers managed by compose |
| `docker compose logs` | View logs of all services |
| `docker compose build` | Build or rebuild services |
| `docker compose exec [service] [command]` | Execute command in a service |
| `docker compose stop/start/restart` | Stop, start, or restart services |
| `docker compose rm` | Remove stopped containers |
| `docker compose images` | List images used by services |
| `docker compose pull/push` | Pull or push images |
| `docker compose config` | Validate docker-compose.yml |
| `docker compose up --scale [service]=[n]` | Scale a service |

---

## 🐳 Docker Volumes

| Command | Description |
| :--- | :--- |
| `docker volume create [name]` | Create a volume |
| `docker volume ls` | List volumes |
| `docker volume inspect [name]` | Inspect a volume |
| `docker volume rm [name]` | Remove a volume |
| `docker run -v [volume]:[path] [image]` | Use volume in a container |

---

## ☸️ Kubernetes & kind Commands

### kubectl config
| Command | Description |
| :--- | :--- |
| `kubectl config current-context` | Show current context |
| `kubectl config use-context [context]` | Switch context |

### kind
| Command | Description |
| :--- | :--- |
| `kind create cluster --name [name]` | Create a new kind cluster |
| `kind create cluster --name [name] --config [file]` | Create cluster with config |
| `kind delete clusters [name]` | Delete a kind cluster |
| `kind get clusters` | List clusters |

### Nodes
| Command | Description |
| :--- | :--- |
| `kubectl get nodes` | List nodes |
| `kubectl get nodes -o wide` | List nodes with details |

### Pods
| Command | Description |
| :--- | :--- |
| `kubectl run [pod] --image [image]` | Create a pod |
| `kubectl apply -f [file]` | Apply manifest |
| `kubectl get pods` | List pods |
| `kubectl get pods -o wide` | List pods with details |
| `kubectl describe pod [pod]` | Show pod details |

### Logs & Exec
| Command | Description |
| :--- | :--- |
| `kubectl logs [pod]` | Show pod logs |
| `kubectl logs [pod] -c [container]` | Show container logs |
| `kubectl exec -it [pod] -c [container] -- bash` | Exec bash in container |
| `kubectl exec -it [pod] -c [container] -- date` | Run command in container |
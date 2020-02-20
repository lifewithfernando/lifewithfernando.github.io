---
title: "[GCP] Understanding about Docker"
date: 2020-02-20 23:59:28 -0400
categories: gcp toyproject docker
---


Understanding about Docker using GCP

Docker에 대한 이해를 위해 GCP로 실습


1. Docker run hello-world
Cloud Shell에서 해당 명령어를 실행했을 때, 도커 데몬이 로컬에서 'hello-world'라는 컨테이너를 찾는다.
로컬에서 해당 컨테이너를 찾을 수 없는 경우, 도커 퍼블릭 레포지토리인 Docker-Hub에서 'hello-world' 컨테이너를 가져와서 실행한다. 이때 컨테이너가 담고 있는 "hello from Docker!"라는 내용을 출력하게 된다.

<img width="1440" alt="docker_01_docker run hello-world" src="https://user-images.githubusercontent.com/61104317/74968562-5cdf0480-545e-11ea-91f3-d1dc671aa58f.png">


2. Docker images / Docker run hello-world
도커 이미지를 확인하게 되면, Docker Hub Repository에서 가져온 이미지를 보여준다. 그리고 다시 한번 처음 명령어를 치면, 같은 "hello from Docker!"라는 내용을 불러오는데, 이때는 로컬 레지스트리에서 가져온 이미지이다.

<img width="1440" alt="docker_02_docker image" src="https://user-images.githubusercontent.com/61104317/74968563-5d779b00-545e-11ea-9e7a-31f092f333b9.png">


3. Docker ps / Docker ps -a
현재 실행 중인 도커 프로세스를 의미한다. 이미 실행된 도커 프로세스 리스트를 불러온다.

<img width="1440" alt="docker_03_docker ps -a" src="https://user-images.githubusercontent.com/61104317/74968566-5e103180-545e-11ea-8f3b-b8d82a194572.png">

"BUILD"
4. 'test' 디렉토리 만들어서 도커파일 생성
  도커 이미지를 node 버전 6을 사용
  컨테이너의 현재 디렉토리 설정
  현재 디렉토리의 있는 내용 컨텐츠를 컨테이너로 추가
  컨테이너에 사용할 포트를 80으로 지정
  app.js 애플리케이션을 실행하기 위해 node를 실행

<img width="1440" alt="docker_04_mkdir test" src="https://user-images.githubusercontent.com/61104317/74968569-5e103180-545e-11ea-82e6-32616abf64ad.png">

5. cat > app.js <<EOF 로 도커파일 내용 확인

<img width="1440" alt="docker_05_cat appjs" src="https://user-images.githubusercontent.com/61104317/74968571-5ea8c800-545e-11ea-86ca-40a7918359e6.png">

6. docker build -t node-app:0.1
  이미지 빌드
  'node-app' 이라는 컨테이너 이름과, 이 컨테이너는 '0.1' 버전으로 태깅이 됨 
  'node-app'(child image)을 실행하게 해주는 베이스 이미지가 'node' 컨테이너 이미지

이후 랩에 나오겠지만, Child image를 지우지 않고, base image를 지울 수 없다.

<img width="1440" alt="docker_06_docker builde node-app01" src="https://user-images.githubusercontent.com/61104317/74968573-5f415e80-545e-11ea-9897-4ac32a6e50bf.png">


"RUN"
7. docker images / docker run -p 4000:80 --name my-app node-app:0.1
  REPOSITORY에 'node-app'(child image), 'node'(base image), 'hello-wordl' 이미지 확인.
  'my-app'으로 웹 서버를 'node-app'의 '0.1'로 태깅된 버전으로 실행을 할 것이고, 서버 포트를 80으로 오픈하고, 호스트의 4000번과 맵핑하겠다.(호스트가 접속 시도할 때 4000번 포트로 접속하면 접속될 것이다)

<img width="1440" alt="docker_07_docker run -p 4000" src="https://user-images.githubusercontent.com/61104317/74968574-5f415e80-545e-11ea-836f-d9d2474b04b9.png">


8. curl http://localhost:4000
서버에 정상적으로 접속되면 'node-app' 이미지에 들어있는 내용이 실행되는 것을 확인할 수 있다.

<img width="1440" alt="docker_08_curl" src="https://user-images.githubusercontent.com/61104317/74968576-5fd9f500-545e-11ea-919d-864deb7b7a78.png">


9. docker stop my-app && docker rm my-app / docker run -p 4000:80 --name my-app -d node-app:0.1 / docker logs [CONTAINER ID]
'my-app' 컨테이너를 중지하고 삭제 / 백그라운드에서 컨테이너를 동작시키기 위해 다시 한번 실행.
컨테이너 ID로 로그 확인

<img width="1440" alt="docker_09_dockerps" src="https://user-images.githubusercontent.com/61104317/74968578-5fd9f500-545e-11ea-9bd1-71ddee6c9566.png">

10. 'app.js' 애플리케이션 수정 

<img width="1440" alt="docker_10_nano appjs" src="https://user-images.githubusercontent.com/61104317/74968579-60728b80-545e-11ea-82d2-1a0f2e6783f6.png">

11. 'app.js' 애플리케이션에서 "Hello from Docker!" 내용 수정

<img width="1440" alt="docker_11_nano appjs2" src="https://user-images.githubusercontent.com/61104317/74968581-610b2200-545e-11ea-9461-e313670d1fff.png">

12. cat app.js
'app.js' 애플리케이션 실행해서 바뀐 내용확인

<img width="1440" alt="docker_12_cat appjs" src="https://user-images.githubusercontent.com/61104317/74968583-610b2200-545e-11ea-8bfa-a4a14d1b740b.png">

13. docker build -t node-app:0.2 . / docker run -p 8080:80 --name my-app-2 -d node-app:0.2
'node-app' 베이스 이미지를 '0.2' 버전으로 태깅해서 현재 디렉토리에 빌드 /
'my-app-2' 컨테이너를 80으로 오픈하는데, 맵핑이되는 호스트의 포트는 8080으로 설정(4000 포트는 이미 사용 중이어서 다른 포트 지정)

<img width="1440" alt="docker_13_docker build02" src="https://user-images.githubusercontent.com/61104317/74968586-61a3b880-545e-11ea-9296-76c0eea4faa6.png">


"PUBLISH"
Google Container Repository에 이미지를 밀어 넣을 것이다

14. docker tag node-app:0.2 gcr.io/[PROJECT ID]/node-app:0.2 / docker image
REPOSITORY에 'gcr.io/[PROJECT ID]/node-app'으로 이미지 생성, 태깅은 '0.2'로 설정
생성된 도커 이미지 리스트 확인

<img width="1440" alt="docker_14_gcr" src="https://user-images.githubusercontent.com/61104317/74968587-623c4f00-545e-11ea-878b-0795f7918405.png">


15. docker push gcr.io/[PROJECT ID]/node-app:0.2
gcr에 이미지 PUSH

<img width="1440" alt="docker_15_docker push" src="https://user-images.githubusercontent.com/61104317/74968588-623c4f00-545e-11ea-9653-b448b8f151c9.png">

16. http://gcr.io/[PROJECT ID]/node-app
GCR에 PUSH한 이미지 웹에서 확인

<img width="1440" alt="docker_16_gcr_node-app" src="https://user-images.githubusercontent.com/61104317/74968589-62d4e580-545e-11ea-89db-fde0a7cb5596.png">

17. 기존에 있는 도커 이미지 모두 삭제 후, gcr에 PUSH한 이미지 가져오는(PULL) 내용 확인
docker stop $(docker ps -q) / docker rm $(docker ps -aq)
> docker rmi node-app:0.2 gcr.io/[project-id]/node-app node-app:0.1
> docker rmi node:6
> docker rmi $(docker images -aq) # remove remaining images
>docker images

<img width="1440" alt="docker_18_docker images" src="https://user-images.githubusercontent.com/61104317/74968594-636d7c00-545e-11ea-818e-54e78c4681b6.png">


18. GCR에서 PUSH한 이미지 가져오고, 백그라운드로 웹 서버 실행해서 접속 후 결과 확인
> docker pull gcr.io/[project-id]/node-app:0.2
> docker run -p 4000:80 -d gcr.io/[project-id]/node-app:0.2
> curl http://localhost:4000

출력내용 "Welcome to Cloud from Fernando"





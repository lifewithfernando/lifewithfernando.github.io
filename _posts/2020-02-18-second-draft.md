---
title: "[AWS] API Gateway 101"
date: 2020-02-18 23:39:28 -0400
categories: aws toyproject apigateway lambdafunction
---

[AWS] API Gateway

Netflix의 서비스 모델 따라잡기 프로젝트 101

AWS에서 제공하는 서비스를 이용한 서비스 모델인 Netflix의 아키텍쳐를 하나씩 살펴보고
최종적으로 모든 서비스들을 통합해서 확인해 보려고 한다.

테스트한 토폴로지이며, 최종적으로 구상하고 싶은 구성과 함께 개략적으로 나타냈다.

이번 테스트에 마이크로 서비스 관련 부분은 추가하지 않았기 때문에 해당 부분은 무시해도 된다.

최종적으로 서비스들을 다 합쳤을 때, 서비스가 이루어지는 그림을 그리고 싶어서 표현해 놓은 것이다.

<img width="799" alt="20200218_topology" src="https://user-images.githubusercontent.com/61104317/74769033-f8d90680-52cc-11ea-81e9-b40ac36e24a1.png">



1. API Gateway
  - 대규모 시스템 구축시에 사용되는 마이크로 서비스 아키텍쳐를 구성시에
  사용자의 요청을 API Gateway가 받아 해당 마이크로 서비스에 요청해서 대신 응답


시스템이 커지고 서비스 요청하는 사용자의 요청이 커짐에 따라, 네트워크 지연과 서버에 부하가 생길 수 있기에 이를 방지하기 위해 등장


##AWS에서 Lambda를 이용하여 API Gateway 설정

API Gateway를 연결하기 위한 Lambda 생성해 줄 것이다.

Lambda Function 페이지

![01_lambda-function](https://user-images.githubusercontent.com/61104317/74764285-c5927980-52c4-11ea-8e27-bcf1266972ff.png)

Function 생성

![02_lambda-create-functions](https://user-images.githubusercontent.com/61104317/74764287-c75c3d00-52c4-11ea-97b1-0dafd9d6d4cf.png)

Lambdaexample이라는 Function 생성
- 생성된 Function을 API Gateway와 연결할 것이다.
- Trigger를 생성하여 'API Gateway' 선택

![03_lambda-create-functions-completion](https://user-images.githubusercontent.com/61104317/74764289-ca572d80-52c4-11ea-9ec4-d78d1c85d584.png)

API Gateway에서 새로운 API를 생성하고, API 종류는 REST API 선택

![04_lambda-add-trigger](https://user-images.githubusercontent.com/61104317/74764291-cc20f100-52c4-11ea-83d4-3702965b1736.png)

API Gateway 설정 완료

![05_labmda-trigger-apigw](https://user-images.githubusercontent.com/61104317/74764298-cdeab480-52c4-11ea-9803-58577105a3fb.png)

Event로 발생시킬 테스트 설정
Resource의 'ANY'로 되어 있는 부분은 어떤 HTTP Method를 사용할 것인지에 대한 설정. 리소스 추가해서 HTTP Method, Get을 사용해서 테스트 진행
![06_labmda-event-template](https://user-images.githubusercontent.com/61104317/74764307-d04d0e80-52c4-11ea-923c-3b15f6fdc73b.png)

Integration Request 설정에 들어가서 Proxy 체크 해제

![08_apigw-proxy해제](https://user-images.githubusercontent.com/61104317/74764320-d6db8600-52c4-11ea-8e65-daa6f0d44368.png)

API Gateway Test
- Response Body에 URL을 접속했을 때 응답할 결과 값을 보여줌

![09_apigw-test](https://user-images.githubusercontent.com/61104317/74764324-d9d67680-52c4-11ea-9d0d-295413ea9bfa.png)

다음의 보이는 주소로 접속해서 테스트 결과값 확인

![10_apigw-urltest](https://user-images.githubusercontent.com/61104317/74764338-dd69fd80-52c4-11ea-9a9e-07c26e06cad9.png)

URL 확인
- 테스트 이벤트로 설정한 람다 값이 호출 되는 것을 확인 "Hello from Lambda!"

![11_apigw-urloutput](https://user-images.githubusercontent.com/61104317/74764340-df33c100-52c4-11ea-8cb7-05e2c521473a.png)

API Gateway로 돌아와서, 다른 경로에 대한 요청 응답을 위한 새 리소스 추가

![12_apigw-create-resource](https://user-images.githubusercontent.com/61104317/74764345-e0fd8480-52c4-11ea-8d0c-733a6d013c09.png)

이름을 'Netflixapigw101'로 지정

![13_apigw-resource-netflixapigw101](https://user-images.githubusercontent.com/61104317/74764349-e2c74800-52c4-11ea-88eb-0c9fb2ed5b2b.png)

리소스 'Netflixapigw101'에 HTTP Method 'Get'추가 후 Lambda Function은 기존에 만들어 놓은 것으로 설정

![14_apigw-method-get](https://user-images.githubusercontent.com/61104317/74764362-e8bd2900-52c4-11ea-9fe8-78f22e02a168.png)

설정 완료되고 난 후의 API 주소 확인

![15_apigw-createdone](https://user-images.githubusercontent.com/61104317/74764368-ea86ec80-52c4-11ea-8ca9-e2890548e430.png)

API Gateway에서 Staging 설정을 'prod'로 설정 후 URL 정상 요청 확인

![16_apigw-prod](https://user-images.githubusercontent.com/61104317/74764373-ec50b000-52c4-11ea-879d-fbd3faefd645.png)


사용자 요청을 API Gateway가 받고 요청한 해당 마이크로 서비스가 응답을 API Gateway로 돌려주고
응답을 다시 사용자에게 돌려줌으로써 부하를 줄일 수 있다.
시스템이 커지면 커질수록 하나의 시스템을 마이크로 서비스로 나누어 하나로 통합해서 운영해야 하기 떄문에
각각의 API 들을 관리할 수 있는 Gateway가 필요하기 때문에 API Gateway가 사용되었다.


끝.

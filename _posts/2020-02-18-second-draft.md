---
title: "[AWS] API Gateway 101"
date: 2020-02-18 23:39:28 -0400
categories: aws toyproject apigateway lambdafunction
---

[AWS] API Gateway

Netflix의 서비스 모델 따라잡기 프로젝트 101

AWS에서 제공하는 서비스를 이용한 서비스 모델인 Netflix의 아키텍쳐를 하나씩 살펴보고
최종적으로 모든 서비스들을 통합해서 확인해 보려고 한다.

1. API Gateway
  - 대규모 시스템 구축시에 사용되는 마이크로 서비스 아키텍쳐를 구성시에
  사용자의 요청을 API Gateway가 받아 해당 마이크로 서비스에 요청해서 대신 응답


시스템이 커지고 서비스 요청하는 사용자의 요청이 커짐에 따라, 네트워크 지연과 서버에 부하가 생길 수 있기에 이를 방지하기 위해 등장


##AWS에서 Lambda를 이용하여 API Gateway 설정

API Gateway를 연결하기 위한 Lambda 생성해 줄 것이다.

Lambda Function 페이지

![01_lambda-function](https://user-images.githubusercontent.com/61104317/74759732-9aa42780-52bc-11ea-81cd-91350531203d.png)

Function 생성
![02_lambda-create-functions](https://user-images.githubusercontent.com/61104317/74759749-a0017200-52bc-11ea-977b-969ed9cd9454.png)

Lambdaexample이라는 Function 생성
- 생성된 Function을 API Gateway와 연결할 것이다
- Trigger를 생성하여 'API Gateway' 선택
![03_lambda-create-functions-completion](https://user-images.githubusercontent.com/61104317/74759770-a55ebc80-52bc-11ea-8d69-7945287b5cc4.png)

API Gateway에서 새로운 API를 생성하고, API 종류는 REST API 선택
![04_lambda-add-trigger](https://user-images.githubusercontent.com/61104317/74759776-a859ad00-52bc-11ea-8edb-3bb1d5013749.png)

API Gateway 설정 완료
![05_labmda-trigger-apigw](https://user-images.githubusercontent.com/61104317/74759792-b0195180-52bc-11ea-8bd3-fb1e11bb4840.png)

Event로 발생시킬 테스트 설정
- Resource의 'ANY'로 되어 있는 부분은 어떤 HTTP Method를 사용할 것인지에 대한 설정. 리소스 추가해서 HTTP Method, Get을 사용해서 테스트 진행
![06_labmda-event-template](https://user-images.githubusercontent.com/61104317/74759802-b4de0580-52bc-11ea-8282-ef4d3e942720.png)

Integration Request 설정에 들어가서 Proxy 체크 해제
![08_apigw-proxy해제](https://user-images.githubusercontent.com/61104317/74759829-bf989a80-52bc-11ea-9228-1e39d9bde4ec.png)

API Gateway Test
- Response Body에 URL을 접속했을 때 응답할 결과 값을 보여줌
![09_apigw-test](https://user-images.githubusercontent.com/61104317/74759840-c32c2180-52bc-11ea-860d-96c8efec653a.png)

다음의 보이는 주소로 접속해서 테스트 결과값 확인
![10_apigw-urltest](https://user-images.githubusercontent.com/61104317/74759844-c58e7b80-52bc-11ea-9769-0fa453a8bf0a.png)

URL 확인
- 테스트 이벤트로 설정한 람다 값이 호출 되는 것을 확인 "Hello from Lambda!"
![11_apigw-urloutput](https://user-images.githubusercontent.com/61104317/74759857-ca532f80-52bc-11ea-95ec-93357fab3f94.png)

API Gateway로 돌아와서, 다른 경로에 대한 요청 응답을 위한 새 리소스 추가
![12_apigw-create-resource](https://user-images.githubusercontent.com/61104317/74759866-cde6b680-52bc-11ea-8681-4c794cfe0ab0.png)

이름을 'Netflixapigw101'로 지정
![13_apigw-resource-netflixapigw101](https://user-images.githubusercontent.com/61104317/74759877-d3440100-52bc-11ea-8ef7-43a7216da1fc.png)

리소스 'Netflixapigw101'에 HTTP Method 'Get'추가 후 Lambda Function은 기존에 만들어 놓은 것으로 설정
![14_apigw-method-get](https://user-images.githubusercontent.com/61104317/74759882-d5a65b00-52bc-11ea-9960-a45937df02d7.png)

설정 완료되고 난 후의 API 주소 확인
![15_apigw-createdone](https://user-images.githubusercontent.com/61104317/74759889-d8a14b80-52bc-11ea-9ae3-bbe164b3cd95.png)

API Gateway에서 Staging 설정을 'prod'로 설정 후 URL 정상 요청 확인
![16_apigw-prod](https://user-images.githubusercontent.com/61104317/74759895-db03a580-52bc-11ea-8cbd-3b02a3bb1e83.png)


사용자 요청을 API Gateway가 받고 요청한 해당 마이크로 서비스가 응답을 API Gateway로 돌려주고
응답을 다시 사용자에게 돌려줌으로써 부하를 줄일 수 있다.
시스템이 커지면 커질수록 하나의 시스템을 마이크로 서비스로 나누어 하나로 통합해서 운영해야 하기 떄문에
각각의 API 들을 관리할 수 있는 Gateway가 필요하기 때문에 API Gateway가 사용되었다.


끝.

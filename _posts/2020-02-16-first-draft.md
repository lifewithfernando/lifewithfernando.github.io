---
title: "[AWS]VPC Peering"
date: 2020-02-17 16:39:28 -0400
categories: aws toyproject 'vpc peering'
---

[AWS] VPC Peering

다음은 해당 랩의 구성도이다.
![20200216_AWS_Topology](https://user-images.githubusercontent.com/61104317/74605836-f16bfe80-510e-11ea-8f62-2010c8bcc6b3.png)

서로 다른 리전의 각각의 VPC끼리 통신하기 위한 방법으로 VPC Peering을 사용하였다.
Oregon(us-west-2)과 N.Virginia(us-east-1)에 각각 VPC와 서브넷을 할당 후, 윈도우 서버, 리눅스 서버 기본 세팅했다.

먼저 Oregon(us-west-2) 설정
1. VPC 설정
<img width="1053" alt="oregon-vpc" src="https://user-images.githubusercontent.com/61104317/74605801-b964bb80-510e-11ea-856d-a2fd5be034c8.png">

2. Subnets 설정
<img width="1055" alt="oregon-subnets" src="https://user-images.githubusercontent.com/61104317/74605816-ce414f00-510e-11ea-9d57-5f37b5fa9cee.png">

3. Routing Table 설정(Peering Connection 설정 후)
<img width="1052" alt="oregon-routing_table" src="https://user-images.githubusercontent.com/61104317/74605818-d13c3f80-510e-11ea-906b-9612d3bdc87f.png">

4. Peering Connection 설정
<img width="1052" alt="oregon-peering_connection" src="https://user-images.githubusercontent.com/61104317/74605820-d4cfc680-510e-11ea-96d7-a7f9ec3aa301.png">

5. Oregon(us-west-2)에 윈도우 서버 인스턴스 생성(각 AZ에 하나씩 생성)
<img width="1054" alt="oregon-win_instances" src="https://user-images.githubusercontent.com/61104317/74605824-de592e80-510e-11ea-9a78-4502eaea89a2.png">

다음 N.Virginia(us-east-1) 설정
1. VPC 설정
<img width="1052" alt="virginia-vpc" src="https://user-images.githubusercontent.com/61104317/74605840-fb8dfd00-510e-11ea-8182-e31052a16445.png">

2. Subnets 설정
<img width="1052" alt="virginia-subnets" src="https://user-images.githubusercontent.com/61104317/74605846-0052b100-510f-11ea-8461-5480627e88e7.png">

3. Routing Table 설정(Peering Connection 설정 후)
<img width="1052" alt="virginia-routing_table" src="https://user-images.githubusercontent.com/61104317/74605848-034da180-510f-11ea-91e5-ad3bf5c4af72.png">

4. Peering Connection 설정
<img width="1052" alt="virginia-peering_connections" src="https://user-images.githubusercontent.com/61104317/74605854-0779bf00-510f-11ea-8d79-ca6e21185f46.png">

5. N.Virginia(us-east-1)에 리눅스 서버 인스턴스 생성(각 AZ에 하나씩 생성)
<img width="1052" alt="virginia-instances" src="https://user-images.githubusercontent.com/61104317/74605856-0b0d4600-510f-11ea-98a1-6ee791f79ad6.png">


Peering 연결했으니 서로 다른 VPC에 있는 인스턴스에서 통신 확인
(라우팅은 각 VPC에 AZ 한 군데만 설정해서 확인했다. 라우팅 설정 참고)

1. Oregon WinSVR(172.31.16.100) -> N.Virginia LinnuxSVR(192.168.16.100)
<img width="1440" alt="oregon2virginia-ping" src="https://user-images.githubusercontent.com/61104317/74605861-12345400-510f-11ea-9491-420fcfba9238.png">

2. N.Virginia LinnuxSVR(192.168.16.100) -> Oregon WinSVR(172.31.16.100)
<img width="757" alt="virginia2oregon-ping" src="https://user-images.githubusercontent.com/61104317/74605860-0fd1fa00-510f-11ea-99f7-645115f7f2b1.png">


자세하게 설정 캡쳐하지 않은 이유는, 기본 설정 관련 부분이기에 생략해도 좋다고 생각했다.
중요한 건 해당 랩 구성, 어떤 테스트를 할 것인지, 그리고 결과에 대한 내용이기 때문이다.

처음 시작. 자정 전에 완료할 수 있었다.
오랜 만에 AWS 구성도를 그려서 조금 어설픈지만, 점차 나아질 것이다.

끝.




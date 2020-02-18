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






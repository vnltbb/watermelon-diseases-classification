# 수박 병해 분류 모델 만들기
- 프로젝트 소스 파일 : [Plant Village disease Classification | Acc: 99.6%] https://www.kaggle.com/code/abdallahwagih/plant-village-disease-classification-acc-99-6 
- 소스 파일을 목적에 맞게 편집해서 이용
- .gitignore의 마지막 부분에 데이터셋 폴더 경로를 상황에 맞게 수정해서 적용하기!

## 패키지 모듈 설치하기 
- 파이썬 버전 3.9 이하 이용하기 : 그 이상 버전에서는 tensorflow 2.9.1 지원하지 않음
- mac M1 / M2 유저는 첫 번째 `pip install tensorflow==2.9.1`을 `pip install tensorflow-macos==2.9.1`로 바꿔서 적용하기 

## 데이터 셋 불러오기
- 사용한 데이터 셋 [sujaykapadnis/watermelon-disease-recognition-dataset] https://www.kaggle.com/datasets/sujaykapadnis/watermelon-disease-recognition-dataset 

# project log
25/04/07 수정하거나 살펴볼 코드 라인에 '⭐️'표시, model save 파트 통합
         모든 파일의 붙어 있는 '⭐️' 표시를 확인 한 다음에 상황에 맞춰 수정한 다음에 사용할 것.
25/04/12 전처리 함수 설정하지 않음. 학습 과정에서 편향 발생한 것으로 보임. 
         efficientNet 전처리 함수 불러와서 적용 완료.
25/04/14 추론 모델 작동 코드라인 전처리 함수 적용.

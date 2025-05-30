# Quest 5

코더  윤원
리뷰어 안진용

🔑 **PRT(Peer Review Template)**

- [ㅇ] **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
  - 문제에서 요구하는 기능이 정상적으로 작동하는지?
    - 해당 조건을 만족하는 부분의 코드 및 결과물을 근거로 첨부
    - https://github.com/dev-ranger/AIFFELL_quest/blob/main/Fluttet/quest05/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-03-13%20%EC%98%A4%ED%9B%84%203.42.10.png?raw=true
    - https://github.com/dev-ranger/AIFFELL_quest/blob/main/Fluttet/quest05/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-03-13%20%EC%98%A4%ED%9B%84%203.42.34.png?raw=true
    - https://github.com/dev-ranger/AIFFELL_quest/blob/main/Fluttet/quest05/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-03-13%20%EC%98%A4%ED%9B%84%203.42.45.png?raw=true
- [ㅇ] **2. 핵심적이거나 복잡하고 이해하기 어려운 부분에 작성된 설명을 보고 해당 코드가 잘 이해되었나요?**
  - 해당 코드 블럭에 doc string/annotation/markdown이 달려 있는지 확인
  - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
  - 주석을 보고 코드 이해가 잘 되었는지 확인
    - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
    - 
      ![a](https://github.com/user-attachments/assets/1c16df31-cd50-4099-97ab-3ec0fdf9f22a)
      ![b](https://github.com/user-attachments/assets/73cdb932-be81-4106-b29d-0de73a35e0fa)
      
      ![c](https://github.com/user-attachments/assets/be81c5ac-7d7a-448c-9fb4-cd81cc2d2d42)
      
      ![e](https://github.com/user-attachments/assets/470bafe0-3dbc-40b1-8ee5-3360261719e2)

          수업 끝나고 로컬환경을 만들어서 해보려고 합니다. 좋은 설명 감사합니다~!
      
- [ㅇ] **3.** 에러가 난 부분을 디버깅하여 “문제를 해결한 기록”을 남겼나요? 또는
  “새로운 시도 및 추가 실험”을 해봤나요? \*\*\*\*
  - 문제 원인 및 해결 과정을 잘 기록하였는지 확인 또는
  - 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도,
    실험이 기록되어 있는지 확인 - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
    
      ![g](https://github.com/user-attachments/assets/05633542-a290-4905-a5ab-01122659e980)

    
- [ㅇ] **4. 회고를 잘 작성했나요?**
  - 프로젝트 결과물에 대해 배운점과 아쉬운점, 느낀점 등이 상세히 기록 되어 있나요?
  - 
    ![f](https://github.com/user-attachments/assets/5d6f1c71-07f6-4783-9a97-a8621854180f)

    
- [ㅇ] **5. 코드가 간결하고 효율적인가요?**
  - 코드 중**복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지**
    - **잘 작성되었다고 생각되는 부분을 근거로** 첨부합니다.
    - 
      ![d](https://github.com/user-attachments/assets/f2c684e0-6e1f-4ea7-8f20-185dd246e9ca)

# Flutter : Setup before Run

1. prepare the images
   /images/quest5/jellyfish.png

2. add text into pubspec.yaml

flutter:
assets: - images/quest5/

3. please change the url
   line : 35
   String url = "https://playcode.com:8443/";
   -> ex ) http://localhost:8000 <-

## 회고

원:

어제 했던 과제와 거의 비슷한 퀘스트가 나왔습니다.
기존 코딩에서 수정할 부분을 조금씩 수정해 나가면서 작성 하였고,
서버의 내용을 변경하고 화면을 구성하는 부분에는 이슈가 없었습니다.
다만 그대로 내려받은 해파리의 png 파일을 그대로 모델에 맡겼더니
에러를 뱉어내어 jpg 로 변경하여 넣어주는 작업을 진행하게 되었네요.

유경:
어제 10개의 스텝을 따라가며 Flutter+ Fastapi로 서비스를 만들때도 어려워서 계속 뒤쳐졌는데,
사진 하나 바뀌었을 뿐인데 같은 Vgg16모델을 적용하는것도 어렵게 느껴졌다.
한가지 모델을 형성해두면 이를 활용해
다양한 이미지들을 예측하는데 사용할 수 있다는 점이 흥미로웠다.
코드로 짜여진 정보를 앞전에 학습했던 화면구현을 통해
사용자친화적인 방법으로 정보를 제공할 수 있는것이 신기하다.
비슷한 구조의 문제인데도 조금만 정보가 달라져도 코드를 헤맨다는 점에서
하나하나를 짚고넘어가는 세세한 공부가 더 필요할 것 같다.
플러터 너무 어렵지만 평소 사용하는 어플들이 어떤 구성을 통해 시각적으로 전달되는지 구조적으로 알 수 있어 좋았다.

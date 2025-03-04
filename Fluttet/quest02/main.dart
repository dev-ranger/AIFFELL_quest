/*
퀘스트 26 앱 화면을 구성해보자!
• 앱을 실행하면 처음 보이는 페이지를 작성합니다.
• 주요 포인트는 다섯 가지입니다.
(X)1. appbar 좌측 상단에 원하는 아이콘을 추가합니다.
-> appbar 마우스를 가져다 대고 매개변수를 확인한 후에 leading 매개변수가 보이길래
그 안에 iCON 추가하고 완료 (끝)
(x)2. appbar 중앙에 “글씨를 왜 만들까”라는 텍스트를 추가합니다.
-> 매우 쉽게 해결
(x) 3. appbar의 색상을 ‘blue’로 지정합니다.
-> appbar 에 마우스커서 가져다 놓고 매개변수 확인한 후에 컬러지정(끝)
(X) 4. 화면 중앙에 “Text”라고 표시된 button을 추가합니다.
해당 버튼을 클릭하면 “버튼이 눌렸습니다.“라는 문장이 DEBUG CONSOLE에 출력되게 합니다.
-> 바람직한 선택은 아니지만 마우스 커서를 많이 가져다 대고 매개변수도 자주 확인했고, 은님이 페이지 215에 있는
Button에 color 설정해주는 방법을 확인해줘서 완료. (끝)
(X) 5. 화면 하단의 중앙에 5개의 container가 중첩됩니다.
각 container는 정사각형이며, 각각의 컨테이너의 크기는 높이와 너비가 60씩 증가합니다.
(가장 바깥 container는 300*300)
-> 기능상으로는 일단 완료

• 크기 정보:
• icon: 186-193
• icon2: 205-210
• stack: 225-233
• stack2: 245
• appbar: 325 */

import 'package:flutter/material.dart';

void main() => runApp(StackApp());

class StackApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Quest',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(
          leading: Icon(Icons.alarm),
          title: Center(child: Text('글씨를 왜 만들까')),
          backgroundColor: Colors.blue,
        ),
        body: Column(
          children: [
            mainButtonArea(),
            Center(child: SizedBox(width: 211, height: 100)),
            Center(
              child: buildSubSqureRedAndGreen(),
            ),
          ],
        ),
      ),
    );
  }

  Column mainButtonArea() {
    return Column(
            children: [
              Container(height: 100),
              SizedBox(
                height: 50,
                child: buildMainTextButton(),
              ),
            ],
          );
  }

  Stack buildSubSqureRedAndGreen() {
    return Stack(
              children: [
                Container(width: 300, height: 300, color: Colors.green),
                Container(width: 240, height: 240, color: Colors.red),
                Container(width: 180, height: 180, color: Colors.green),
                Container(width: 120, height: 120, color: Colors.red),
                Container(width: 60, height: 60, color: Colors.green),
              ],
            );
  }

  TextButton buildMainTextButton() {
    return TextButton(
                  onPressed: showMessage,
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(
                      Color(Colors.red.value),
                    ),
                  ),
                  child: Text("Text"),
                );
  }
}
void showMessage() {
  print('버튼이 눌렸습니다.');
}

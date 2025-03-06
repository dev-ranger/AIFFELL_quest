import 'package:flutter/material.dart';

//
// 네비게이션 만들기
//
// main - 1,2 네비게이션 설정
// 1page  고양이 (pushNamed)
// 2page 개 (pop)

import 'package:font_awesome_flutter/font_awesome_flutter.dart';

void main() => runApp(CatPage());

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: "/first",
      routes: {
        "/first": (context) => CatPage(),
        "/second": (context) => DogPage(),
      },
    );
  }
}

/*
Todo.

SecondPage
[X] •	appbar 좌측 상단에 원하는 아이콘을 추가합니다(강아지모양이면 좋겠어요!).
[X] •	appbar 중앙에 “Second Page”라는 텍스트를 추가합니다.
[X] •	화면 중앙에 “Back”이라고 표기된 button을 추가합니다. 해당 버튼을 클릭하면
[X] •	생성했던 페이지 stack을 삭제합니다.
[X]•	is_cat을 true 바꿔서 전달합니다.
[X]•	화면 하단의 중앙에 강아지 이미지를 출력합니다. (300*300)
[X] •	이미지를 누르면 is_cat의 현재 상태가 DEBUG CONSOLE에 출력되게 합니다.
 •	화면 전환, 데이터 전달 339-379(아... 책에서.. )
*/
class DogPage extends StatelessWidget {
  late bool isCat;

  @override
  Widget build(BuildContext context) {
    isCat = getArgs(context);

    return MaterialApp(
      title: 'dog',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(
          leading: Icon(FontAwesomeIcons.dog),
          title: Center(child: Text('Second Page')),
        ),
        body: Column(
          children: <Widget>[
            SizedBox(height: 150),
            buildBackButton(context),
            Center(
              child: GestureDetector(
                onTap: () {
                  debugPrint("Current State of isCat : $isCat ");
                },
                child: SizedBox(
                  width: 300,
                  height: 300,
                  child: Image.asset("images/dog2.jpeg"),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  bool getArgs(BuildContext context) {
    Object? args = ModalRoute.of(context)?.settings.arguments;
    if (args != null) {
      return ModalRoute.of(context)?.settings.arguments as bool;
    } else {
      return false;
    }
  }

  ElevatedButton buildBackButton(BuildContext context) => ElevatedButton(
    onPressed: () {
      isCat = true;
      Navigator.pop(context, isCat);
    },
    child: Text("Back"),
  );
}

/*
Todo.
FirstPage
[X] •	appbar 좌측 상단에 원하는 아이콘을 추가합니다(고양이 모양이면 좋겠어요!).
[X] •	appbar 중앙에 “First Page”라는 텍스트를 추가합니다.
[X] •	is_cat 변수를 만듭니다. Boolean이고, 초기값은 true로 설정합니다.
-> is_cat 은 변수 표기 rule 에 안 맞아서 isCat 이라고 작성
[X] •	화면 중앙에 “Next”라고 표기된 button을 추가합니다. 해당 버튼을 클릭하면:
[X] •	is_cat을 false로 초기화합니다.
[X] •	초기화된 변수를 is_cat을 다음 페이지로 전달합니다.
[X] •	화면 하단의 중앙에 고양이 이미지를 출력합니다. (300*300)
[X] •	이미지를 누르면 is_cat의 현재 상태가 DEBUG CONSOLE에 출력되게 합니다.*/
class CatPage extends StatelessWidget {
  late bool isCat = false;

  @override
  Widget build(BuildContext context) {
    isCat = getArgs(context);

    return MaterialApp(
      title: 'cat',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(
          leading: Icon(FontAwesomeIcons.cat),
          title: Center(child: Text('First Page')),
        ),
        body: Column(
          children: <Widget>[
            SizedBox(height: 150),
            buildNextButton(context),
            Container(child: buildTouchImage(context)),
          ],
        ),
      ),
    );
  }

  GestureDetector buildTouchImage(BuildContext context) {
    return GestureDetector(
      // onTap: () {
      //   debugPrint("Current State of isCat : $isCat ");
      // },
      child: SizedBox(
        width: 300,
        height: 300,
        child: Image.asset("images/cat1.jpeg"),
      ),
    );
  }

  ElevatedButton buildNextButton(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        Navigator.of(context).pushNamed("/second", arguments: isCat);
      },
      child: Text('Next'),
    );
  }

  bool getArgs(BuildContext context) {
    Object? args = ModalRoute.of(context)?.settings.arguments;
    if (args != null) {
      debugPrint("args : $args");
      return ModalRoute.of(context)?.settings.arguments as bool;
    } else {
      return false;
    }
  }
}

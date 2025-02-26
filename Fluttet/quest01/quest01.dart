import 'dart:async';
import 'dart:collection';

abstract class Cycle {
  int getDuration();
  String getType();
}

class Work extends Cycle {
  static const String type = "Working";
  late int duration;
  Work(this.duration);

  @override
  int getDuration() {
    return this.duration;
    throw UnimplementedError();
  }

  @override
  String getType() {
    return type;
  }
}

class Rest extends Cycle {

  static const String type = "Rest";
  late int duration;

  Rest(this.duration);

  @override
  int getDuration() {
    return this.duration;
    throw UnimplementedError();
  }

  @override
  String getType() {
    return type;
  }
}


class PomodoroTimer {
  late Queue<Cycle> _cycles;
  PomodoroTimer(this._cycles);

  void add(Cycle cycle) {
    this._cycles.add(cycle);
  }

  Cycle getCycle(){
    Cycle returnCycle = this._cycles.first;
    this._cycles.removeFirst();
    return returnCycle;
  }
  void working() {
    DateTime startedTime = DateTime.now();
    //Test is it work the Time function

    if(_cycles.isEmpty){
      print("empty cycle");
    }else{
      Cycle workingCycle = getCycle();
      print("Start  ! ${workingCycle.getType()} ");

      Timer.periodic(const Duration(seconds: 1), (t) {
        DateTime currentTime = DateTime.now();
        int spendTime = currentTime
            .difference(startedTime)
            .inSeconds;

        print("spendTime : $spendTime , [${currentTime.hour}: ${currentTime.minute}: ${currentTime.second}]");
        if (spendTime >= workingCycle.getDuration()) {
          if(_cycles.isEmpty){
            t.cancel();
          }
          workingCycle = getCycle();
          startedTime = currentTime;
          spendTime = 0;
          print("Start  ! ${workingCycle.getType()} ");
        }
      });
    }
  }
}

main() {
  // 1. Pomodoro timer 정의
  const int WORK_DURATION = 25;
  const int REST_DURATION = 5;
  const int SPECIAL_REST_DURATION = 15;
  final Queue<Cycle> cycles = Queue();

  cycles.add(Work(WORK_DURATION));
  cycles.add(Rest(REST_DURATION));
  cycles.add(Work(WORK_DURATION));
  cycles.add(Rest(REST_DURATION));
  cycles.add(Work(WORK_DURATION));
  cycles.add(Rest(REST_DURATION));
  cycles.add(Work(WORK_DURATION));
  cycles.add(Rest(SPECIAL_REST_DURATION));

  PomodoroTimer pomodoroTimer = PomodoroTimer(cycles);

  pomodoroTimer.working();

}


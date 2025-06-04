import 'dart:async';
import 'dart:convert';

abstract class LiveWidget {
  void display() {
    print("Rendering a base widget");
  }
}

class BasicLabelWidget extends LiveWidget {
  @override
  void display() {
    super.display();
    print("label displayed in basic!");
  }
}

class Fancylabelwidget extends LiveWidget {
  @override
  void display() {
    print("Fancy label displayed in style!");
  }
}

class Button {
  String label;
  Button(this.label);
  void click() {
    print("$label button clicked!");
  }
}

class TextWidget {
  String? text;
  TextWidget({this.text});
  void render() {
    print("Rendering text:$text");
  }
}

class User {
  String? name;
  int? age;
  User({required this.name, required this.age});
  showUser() {
    print("Name : $name, Age : $age");
  }
}

Future<void> fetchdata() async {
  print("Fetching data...");
  await Future.delayed(Duration(seconds: 2));
  print("Data retrieved!");
}

void startApp() {
  print("Welcome to Dart!");
}

void showAppInfo() {
  print("This is dart Application ");
}

void Json() {
  Map<String, dynamic> product = {"id": 1, "name": "Labtop", "price": 1220.5};
  String jsonString = jsonEncode(product);
  print("JSON String: $jsonString");
  Map<String, dynamic> parsedMap = jsonDecode(jsonString);
  print("JSON map $parsedMap");
}

void main() {
  BasicLabelWidget basic = new BasicLabelWidget();
  basic.display();
  Fancylabelwidget fancy = new Fancylabelwidget();
  fancy.display();
}

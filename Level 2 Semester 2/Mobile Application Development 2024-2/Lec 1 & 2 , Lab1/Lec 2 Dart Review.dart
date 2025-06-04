//
void main() {
  //1-print
  //print('hello');
  //2-datatypes [int, double, String, bool,
  //           List, Map, var, dynamic]
  /*int num = 5;
  List<int> lst = [1,2,3,4];
  print(lst);
  print('Hello $num');*/

  /*List lst = [1, 2, 3, 'a'];
  print(lst);
  print(lst[0]);

  Map<String, int> m = {'a': 1, 'b': 2};
  print(m);
  print(m['a']);

  List<int> lst2 = [];
  lst2.add(1);//add single value
  lst2.addAll([2,3,4]); //add multi values
  print(lst2);*/

  //3-modifiers [const, final]
  //const x = 10;
  //x = 14;// error [can't change const value]
  //const >> executed in compile time
  //final >> executed in run time

  //4-Arithmetic operators[+-*/ ~/ % ++ --]

  /*int x = 10;
  print(++x);//pre
  print(x++);//post
  */

  // ~/ >> divide and return int value

  //5-Relational operator [> < >= <= == !=]

  //6-type test operator [is is!] ex. var is type

  /*var x = 7;
  print(x is! String);*/

  //7-convert datatype to nullable [?]
  /*int? x;
  print(x);*/

  //8-??value [if null use value]

  /*int? x;
  print(x ?? 10); //if x is null use 10
  print(x);
  int z = x ??= 10; //if x is null, put 10 in x and use 10
  print(x);
*/
  //9-Conditional operator [? value:value]
  /*int x = 10;
  int z = x>10?5:0;*/

  //10-switch
  /*int y = 10;
  switch(y){
    case 1:print('good');break;
  }*/

  //if condition
  /*if(true)
  ;
  else if(true);
  else{
    
  }
  */
  //11-functions
  //print(sum(x:4,y:5));//can use param name then value

  //12-functions: optional parameters [] or {}
  //13-loops

  /*
  //dynamic >> can hold different value types && executed at runtime
  dynamic y = 10;
  y = 'ahmed';
  
  //var hold one value type && executed at compile time
  var x = 10;
  x = "ahmed";
  */

  //foreach >> for

  //14-loops on List and Map
  /*List lst = [1, 2, 3, 4, 5, 6];
  for (var item in lst) print(item);
  lst.forEach((item)=>print(item));*/
  //(params)=>statment [arrow function]

  /*Map<String, int> lst = {'a': 1, 'b': 2};
  for (var item in lst.keys) print(lst[item]);
  lst.forEach((k, v) => print('$k:$v'));*/

  //15-Classes & objects

  //16-Constructors

  Student s1 = Student(1,'ahmed', 27);
  
  //17-static
  //18-inheritance
  //19-implements
  //20-flutter(First APP)
}

class Student {
  int? id;
  String? name;
  double? age;
  Student(id, name, age) {
    this.id = id;
    this.name = name;
    this.age = age;
  }
  void Display() {
    print('$id:$name:$age');
  }
}

/*int sum([int x = 0, int y = 0]) {
  return x + y;
}*/

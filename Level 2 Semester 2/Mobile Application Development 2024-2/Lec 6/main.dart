import 'package:flutter/material.dart';

void main() {
  //runApp(MaterialApp(home: MainApp()));
  runApp(
    MaterialApp(
      initialRoute: "/",
      routes: {
        '/': (context) => MainApp(),
        '/second': (context) => SecondPage(),
        '/third': (context) => ThirdPage(data: "passed from Named Routes"),
      },
    ),
  );
}

class MainApp extends StatefulWidget {
  MainApp({super.key});

  @override
  State<MainApp> createState() => _MainAppState();
}

class _MainAppState extends State<MainApp> {
  int x = 0;
  bool b = false;

  Widget GetSideBar() {
    return Drawer(
      child: ListView(
        children: [
          ListTile(
            title: Text("Home"),
            onTap: () {
              Navigator.pushNamed(context, '/');
            },
          ),
          ListTile(
            title: Text("page 2"),
            onTap: () {
              Navigator.pushNamed(context, '/second');
            },
          ),
          ListTile(
            title: Text("page 3"),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder:
                      (context) => ThirdPage(data: "passed data from sidebar"),
                ),
              );
            },
          ),
        ],
      ),
    );
  }

  Widget CounterPart() {
    return Row(
      children: [
        Spacer(flex: 1),
        Center(
          child: Text(
            '$x',
            style: TextStyle(
              color: Colors.red,
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.blue,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            setState(() {
              x++;
            });
          },
          child: Text("click me"),
        ),
        Spacer(flex: 1),
      ],
    );
  }

  Widget Buttons_StackNavigation() {
    return Row(
      children: [
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.red,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SecondPage()),
            );
          },
          child: Text("page2 stacked"),
        ),
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.red,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder:
                    (context) =>
                        ThirdPage(data: "passed data navigator stacked"),
              ),
            );
          },
          child: Text("page3 stacked"),
        ),
        Spacer(flex: 1),
      ],
    );
  }

  Widget Buttons_NamedNavigation() {
    return Row(
      children: [
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.red,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.pushNamed(context, '/second');
          },
          child: Text("page2 named"),
        ),
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.red,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.pushNamed(context, '/third');
          },
          child: Text("page3 named"),
        ),
        Spacer(flex: 1),
      ],
    );
  }

  Widget Buttons_TabsPage() {
    return Row(
      children: [
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.red,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => PageWithTabs()),
            );
          },
          child: Text("page with tabs"),
        ),
        Spacer(flex: 1),
      ],
    );
  }

  Widget LongPressButton() {
    return ElevatedButton(
      onPressed: () {
        print("Normal Tap");
      },
      child: GestureDetector(
        onLongPress: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => ThirdPage(data: "from long press"),
            ),
          );
        },
        child: Text("Long Press to Go to Page 3"),
      ),
    );
  }

  Widget  Buttons_LoginPage() {
    return Row(
      children: [
        Spacer(flex: 1),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.green,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => LoginPage()),
            );
          },
          child: Text("Login page"),
        ),
        Spacer(flex: 1),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("this is main page")),
      drawer: GetSideBar(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          Spacer(flex: 5),
          CounterPart(),
          Spacer(flex: 2),
          Buttons_StackNavigation(),
          Spacer(flex: 1),
          Buttons_NamedNavigation(),
          Spacer(flex: 1),
          Buttons_TabsPage(),
          Spacer(flex: 1),
          LongPressButton(),
          Spacer(flex: 1),
          Buttons_LoginPage(),
          Spacer(flex: 9),
        ],
      ),
    );
  }
}

class SecondPage extends StatelessWidget {
  const SecondPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Second page")),
      body: Center(
        child: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back_ios_rounded),
        ),
      ),
    );
  }
}

class ThirdPage extends StatelessWidget {
  final String data;
  const ThirdPage({required this.data});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(data)),
      body: Center(
        child: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back_ios_rounded),
        ),
      ),
    );
  }
}

class PageWithTabs extends StatefulWidget {
  const PageWithTabs({super.key});

  @override
  State<PageWithTabs> createState() => _PageWithTabsState();
}

class _PageWithTabsState extends State<PageWithTabs> {
  int selectedIndex = 0;

  // Screens for each tab
  final List<Widget> pages = [
    Center(child: Text('Like Home Page', style: TextStyle(fontSize: 24))),
    Center(child: Text('Like Settings Page', style: TextStyle(fontSize: 24))),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bottom Navigation Example")),
      body: pages[selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
        currentIndex: selectedIndex,
        onTap: (int index) {
          setState(() {
            selectedIndex = index;
          });
        },
      ),
    );
  }
}

class LoginPage extends StatefulWidget {
  LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();

  final TextEditingController emailController = TextEditingController();

  void _showSuccessDialog({required String val}) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text("Success"),
          content: Text("Login Successful with email = $val"),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
                emailController.clear();
              },
              child: Text("OK"),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login Page")),

      body: Padding(
        padding: const EdgeInsets.all(50.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: "Email"),
                validator: (value) => value!.isEmpty ? "Enter email" : null,
                controller: emailController,
              ),
              SizedBox(height: 20), 
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    _showSuccessDialog(val: emailController.text);
                  }
                },
                child: Text("Login"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

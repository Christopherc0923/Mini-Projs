#include <iostream>
#include <string>
#include <vector>
using namespace std;


// template are used as universal type functions, so it can be applied to strings, int, float, double, etc.
template <typename T>
T funMax(T x, T y){
    if (x > y){
        return true;
    };
    return false;
};

int main(){
    cout << "Hello World!" << endl;
    string name;
    
    cout << "Please give me your name: " << endl;
    getline(cin, name);
    cout << "Name: " << name << endl;

    vector<int> v1 {2, 5, 6};
    cout << v1[1] << endl;
    int x = 10;
    int y = 12;
    cout << funMax(x, y) << endl;

    struct Person{
        int age;
        string name;
    };

    Person a;
    a.age = 22;
    a.name = "Chris";

    cout << a.name << endl;

}

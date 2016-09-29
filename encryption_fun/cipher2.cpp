#include <iostream>
#include <fstream>

using namespace std;
int main(){
	ifstream myfile;
	myfile.open("cipher2.txt");
	string line;
	getline(myfile, line);
	cout << (line << 20);
	return 0;
}
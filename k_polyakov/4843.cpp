
#include <iostream>
using namespace std;
#include <fstream>
#include <vector>


bool unusual(int x) {
	if (x > 0) { return false; }
	else {
		int s = 0;
		int t = -x;
		while (t > 0) { s += t % 3; t /= 3; }

		if (s == 12) { return true; }
		else return false;
	}
}



int main()
{
	fstream f;
	f.open("C:/Users/lenya/Desktop/27-я задача/С++/27/27-90b.txt");
	int m, total_s, N, x, u_count, K, D, total_len;
	total_s = 0; total_len = 0;
	u_count = 0; m = 0;
	f >> N >> K >> D;
	vector  < vector <int> > prefix_s(K, vector<int>(D, 100000000));
	for (int i = 0; i < N; i++) {
		total_len++;
		f >> x;
		total_s += x;
		if (unusual(x) == true) { ++u_count; }
		if (((prefix_s[u_count % K][total_len % D] != 100000000))) {
			m = max(m, total_s - prefix_s[u_count%K][total_len%D]); }
		prefix_s[u_count % K][total_len % D] = min(prefix_s[u_count % K][total_len % D], total_s);
	}
	cout << m;
}


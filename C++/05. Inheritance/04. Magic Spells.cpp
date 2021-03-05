// Problem: https://www.hackerrank.com/challenges/magic-spells/problem
// Score: 40

// PROVIDED CODE BY HACKERRANK
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Spell {
	private:
		string scrollName;
	public:
		Spell(): scrollName("") { }
		Spell(string name): scrollName(name) { }
		virtual ~Spell() { }
		string revealScrollName() {
			return scrollName;
		}
};

class Fireball : public Spell { 
	private: 
		int power;

	public:
		Fireball(int power): power(power) { }
		void revealFirepower(){
			cout << "Fireball: " << power << endl;
		}
};

class Frostbite : public Spell {
	private: 
		int power;
	public:
		Frostbite(int power): power(power) { }
		void revealFrostpower(){
			cout << "Frostbite: " << power << endl;
		}
};

class Thunderstorm : public Spell { 
	private: 
		int power;
	public:
		Thunderstorm(int power): power(power) { }
		void revealThunderpower(){
			cout << "Thunderstorm: " << power << endl;
		}
};

class Waterbolt : public Spell { 
	private: 
		int power;
	public:
		Waterbolt(int power): power(power) { }
		void revealWaterpower(){
			cout << "Waterbolt: " << power << endl;
		}
};

class SpellJournal {
	public:
		static string journal;
		static string read() {
			return journal;
		}
}; 
string SpellJournal::journal = "";

// SOLUTION START
void counterspell(Spell *spell) {
	auto *x0 = dynamic_cast<Fireball*>(spell);
	if (x0) { x0->revealFirepower(); return ;}
	auto *x1 = dynamic_cast<Frostbite*>(spell);
	if (x1) {x1->revealFrostpower(); return ;}
	auto *x2 = dynamic_cast<Thunderstorm*>(spell);
	if (x2) {x2->revealThunderpower(); return ; }
	auto *x3 = dynamic_cast<Waterbolt*>(spell);
	if (x3) {x3->revealWaterpower(); return; }
	
	string a = spell->revealScrollName(), b = SpellJournal::read();
	int m = a.size(), n = b.size();
	vector<vector<int> > s(m+1, vector<int>(n+1, 0));
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++)
			s[i+1][j+1] = max(s[i][j]+(a[i]==b[j]), max(s[i+1][j], s[i][j+1]));
	}
	cout << s[m][n] << '\n';
	
}
// SOLUTION END

// PROVIDED CODE BY HACKERRANK
class Wizard {
	public:
		Spell *cast() {
			Spell *spell;
			string s; cin >> s;
			int power; cin >> power;
			if(s == "fire") {
				spell = new Fireball(power);
			} else if(s == "frost") {
				spell = new Frostbite(power);
			} else if(s == "water") {
				spell = new Waterbolt(power);
			} else if(s == "thunder") {
				spell = new Thunderstorm(power);
			} else {
				spell = new Spell(s);
				cin >> SpellJournal::journal;
			}
		return spell;
	}
};

int main() {
	int T;
	cin >> T;
	Wizard Arawn;
	while(T--) {
		Spell *spell = Arawn.cast();
		counterspell(spell);
	}
	return 0;
}
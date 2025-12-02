#include <iostream>
#include <string>

using namespace std;
// Function to encode a string to Morse code
string encodeToMorse(const string &text) {
    const string morseCode[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
    string morseText = "";

    for (char c : text) {
        if (isalpha(c)) {
            c = toupper(c);
            morseText += morseCode[c - 'A'] + " ";
        } else if (isdigit(c)) {
            morseText += morseCode[c - '0' + 26] + " "; // Assuming digits are encoded after letters
        } else if (c == ' ') {
            morseText += "/ "; // Using '/' to represent space between words
        }
    }
    return morseText;
    
}
int main() {
    string input;
    cout << "Enter text to encode to Morse code: ";
    getline(cin, input);

    string morseOutput = encodeToMorse(input);
    cout << "Morse Code: " << morseOutput << endl;

    return 0;
}
// save morsecode to .txt file 
#include <fstream>
void saveToFile(const string &morseText) {
    ofstream outFile("morsecode.txt");
    if (outFile.is_open()) {
        outFile << morseText;
        outFile.close();
        cout << "Morse code saved to morsecode.txt" << endl;
    } else {
        cout << "Error opening file for writing." << endl;
    }
}



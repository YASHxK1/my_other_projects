#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

// Function to decode Morse code to text
string decodeFromMorse(const string &morseText) {
    // Create a map for Morse code to character conversion
    map<string, char> morseToChar = {
        {".-", 'A'}, {"-...", 'B'}, {"-.-.", 'C'}, {"-..", 'D'}, {".", 'E'},
        {"..-.", 'F'}, {"--.", 'G'}, {"....", 'H'}, {"..", 'I'}, {".---", 'J'},
        {"-.-", 'K'}, {".-..", 'L'}, {"--", 'M'}, {"-.", 'N'}, {"---", 'O'},
        {".--.", 'P'}, {"--.-", 'Q'}, {".-.", 'R'}, {"...", 'S'}, {"-", 'T'},
        {"..-", 'U'}, {"...-", 'V'}, {".--", 'W'}, {"-..-", 'X'}, {"-.--", 'Y'},
        {"--..", 'Z'},
        // Numbers
        {"-----", '0'}, {".----", '1'}, {"..---", '2'}, {"...--", '3'},
        {"....-", '4'}, {".....", '5'}, {"-....", '6'}, {"--...", '7'},
        {"---..", '8'}, {"----.", '9'}
    };
    
    string decodedText = "";
    stringstream ss(morseText);
    string morseChar;
    
    while (ss >> morseChar) {
        if (morseChar == "/") {
            decodedText += " "; // '/' represents space between words
        } else if (morseToChar.find(morseChar) != morseToChar.end()) {
            decodedText += morseToChar[morseChar];
        } else {
            // Handle unknown Morse code sequences
            decodedText += "?";
        }
    }
    
    return decodedText;
}

// Function to read Morse code from file
string readFromFile(const string &filename) {
    ifstream inFile(filename);
    string morseText = "";
    string line;
    
    if (inFile.is_open()) {
        while (getline(inFile, line)) {
            morseText += line + " ";
        }
        inFile.close();
        cout << "Morse code read from " << filename << endl;
    } else {
        cout << "Error opening file for reading." << endl;
    }
    
    return morseText;
}

// Function to save decoded text to file
void saveDecodedToFile(const string &decodedText) {
    ofstream outFile("decoded_text.txt");
    if (outFile.is_open()) {
        outFile << decodedText;
        outFile.close();
        cout << "Decoded text saved to decoded_text.txt" << endl;
    } else {
        cout << "Error opening file for writing." << endl;
    }
}

int main() {
    int choice;
    string input, decodedOutput;
    
    cout << "Morse Code Decoder" << endl;
    cout << "1. Enter Morse code manually" << endl;
    cout << "2. Read Morse code from file (morsecode.txt)" << endl;
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;
    cin.ignore(); // Clear the input buffer
    
    if (choice == 1) {
        cout << "Enter Morse code to decode (use spaces between letters and '/' between words): ";
        getline(cin, input);
        decodedOutput = decodeFromMorse(input);
    } else if (choice == 2) {
        input = readFromFile("morsecode.txt");
        if (!input.empty()) {
            decodedOutput = decodeFromMorse(input);
        } else {
            cout << "No Morse code found in file." << endl;
            return 1;
        }
    } else {
        cout << "Invalid choice." << endl;
        return 1;
    }
    
    cout << "Decoded Text: " << decodedOutput << endl;
    
    // Ask if user wants to save to file
    char saveChoice;
    cout << "Do you want to save the decoded text to a file? (y/n): ";
    cin >> saveChoice;
    
    if (saveChoice == 'y' || saveChoice == 'Y') {
        saveDecodedToFile(decodedOutput);
    }
    
    return 0;
}
#include <ctime>
#include <fstream>
#include <iostream>

//Moves a file to "/var/www/html/" to be hosted by Apache for remote deployment
//intended for use on linux systems 
//Networking and Apache configuration are not performed by this program

//Generates a random hex string to use as the file name
std::string genRandomName()
{
    std::srand(std::time({}));

    char usableCharacters[] = "0123456789ABCDEF";

    std::string randomName;

    int nameLength;
    nameLength = 32;
    for(int i = 0; i < nameLength; i++)
    {
        randomName += usableCharacters[std::rand() % 16];
    }

    std::string outFilePath;
    outFilePath = "/var/www/html/" + randomName;
    std::cout << "\nyour file is now hosted at:\n";
    std::cout << "\nhttp://[your-IP-Address]/" << randomName << "\n\n"; 
    
    return outFilePath;
}

std::ifstream readFile(std::string fileName)
{
    std::ifstream inFile{fileName};

    if(!inFile)
    {
        std::cerr << "Could not open " << fileName << " for reading.\n";
        std::cerr << "Please try again.\n";
        std::cerr << "Exiting.\n";
        exit;
    }
    
    return inFile;
}

int writeFile(std::string inFileName, std::string outFilePath)
{

    std::ifstream inFile{readFile(inFileName)};
    
    std::ofstream outFile{outFilePath};

    if(!outFile)
    {
        std::cerr << "Could not open " << outFilePath << " for writing.\n";
        std::cerr << "Please try again with higher permissions.\n";
        return 1;
    }

    std::string currentLine;
    while(std::getline(inFile, currentLine))
    {
        outFile << currentLine << "\n";
    }

    return 0;
}



int main()
{

    std::string fileName;
    std::cout << "Enter file to post:\n";
    std::cin >> fileName;

    std::string outPath;
    outPath = genRandomName();

    if(writeFile(fileName, outPath) == 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

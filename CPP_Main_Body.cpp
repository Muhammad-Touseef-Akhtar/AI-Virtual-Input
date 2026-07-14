#include<iostream>
#include <winsock2.h> 
#include <windows.h>
#include "Keyboard_KeyReceiver.h"  
using namespace std;

//--------------------------------------------------------------------------------------------------

#pragma comment(lib, "ws2_32.lib") 


int main()
 {
    WSADATA win_network_drivers;
    WSAStartup(MAKEWORD(2, 2), &win_network_drivers);

    SOCKET communication_antenna = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    
    sockaddr_in portConfig;
    portConfig.sin_family = AF_INET;
    portConfig.sin_port = htons(5005); 
    portConfig.sin_addr.S_un.S_addr = ADDR_ANY;

    bind(communication_antenna, (sockaddr*)&portConfig, sizeof(portConfig));

      cout << "C++ Active. Listening for Hand Signals on Port 5005..." << endl;

    char networkBuffer[1024]; 
    sockaddr_in senderDetails; 
    int senderSize = sizeof(senderDetails);

   while(true)
   { 
        memset(networkBuffer, 0, 1024); 

        int bytesCaught = recvfrom(communication_antenna, networkBuffer, 1024, 0, (sockaddr*)&senderDetails, &senderSize);

         if (bytesCaught > 0) 
        {
             string command_word(networkBuffer);

            if (command_word == "EXIT")
            { 
                cout  << endl << "Exit signal received from Python. Closing server cleanly..." << endl;
                break;
            }

            else if (command_word == "NUM_0")
             pressing_keyboard_key(0x30); 

            else if (command_word == "NUM_1")
             pressing_keyboard_key(0x31); 

            else if (command_word == "NUM_2")
             {pressing_keyboard_key(0x32); 
              cout << "signal send perfectly";}

            else if (command_word == "NUM_3") 
              pressing_keyboard_key(0x33); 

            else if (command_word == "NUM_4")
              pressing_keyboard_key(0x34); 

            else if (command_word == "NUM_5")
              pressing_keyboard_key(0x35);

            else if (command_word == "NUM_6") 
              pressing_keyboard_key(0x36); 

            else if (command_word == "NUM_7")
              pressing_keyboard_key(0x37); 
            else if (command_word == "NUM_8")
              pressing_keyboard_key(0x38); 

            else if (command_word == "NUM_9") 
              pressing_keyboard_key(0x39);

            else if (command_word == "BACKSPACE")
              pressing_keyboard_key(0x08);

        }
    }
    
    cout << "Cleaning up network sockets..." << endl;
    closesocket(communication_antenna);
    WSACleanup();
    cout << "C++ Program Terminated Successfully." << endl;
    return 0;
}




#include <windows.h>
#include<iostream>
#define WIN32_LEAN_AND_MEAN
#include "Keyboard_KeyReceiver.h"
using namespace std;

//---------------------------------------------------------------------------------------------------

void pressing_keyboard_key(WORD virtualKeyCode) 
{
    INPUT keyEvent = { 0 };
    keyEvent.type = INPUT_KEYBOARD;
    keyEvent.ki.wVk = virtualKeyCode;

    keyEvent.ki.dwFlags = 0; 
    SendInput(1, &keyEvent, sizeof(INPUT));

    keyEvent.ki.dwFlags = KEYEVENTF_KEYUP; 
    SendInput(1, &keyEvent, sizeof(INPUT));
}
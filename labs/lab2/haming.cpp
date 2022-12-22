#include <iostream>

using namespace std;

int main()
{
    string kod;
    cin >> kod;
    cout << "Полученное сообщение: " << kod << endl;
    bool S1, S2, S3;
    S1 = kod[0] xor kod[2] xor kod[4] xor kod[6];
    S2 = kod[1] xor kod[2] xor kod[5] xor kod[6];
    S3 = kod[3] xor kod[4] xor kod[5] xor kod[6];
    int S = S3 * 2 * 2 + S2 * 2 + S1;
    if (S == 0)
    {
        cout << "Получившееся правильное сообщение: " << kod << endl;
        cout << "Нет ошибок";
    }
    else
    {
        if (kod[S - 1] == '0')
        {
            kod.replace(S - 1, 1, "1");
        }
        else
        {
            kod.replace(S - 1, 1, "0");
        }

        cout << "Получившееся правильное сообщение: " << kod << endl;
        cout << "ошибка заключается в ";
        switch (S)
        {
        case 1:
            cout << "r1";
            break;
        case 2:
            cout << "r2";
            break;
        case 3:
            cout << "i1";
            break;
        case 4:
            cout << "r3";
            break;
        case 5:
            cout << "i2";
            break;
        case 6:
            cout << "i3";
            break;
        case 7:
            cout << "i4";
            break;
        }
    }
    return 0;
}

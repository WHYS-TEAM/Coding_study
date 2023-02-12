/*****************************************
**  https://school.programmers.co.kr/learn/courses/30/lessons/42885
**  프로그래머스 코딩테스트 : 구명보트
**  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
*****************************************/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    const int MAX_WEIGHT = limit;
    
    int nNumBoat = 0;
    int nFrtOrd = 0;
    int nBckOrd = people.size() - 1;
    
    // Sort Asc Order
    sort(people.begin(), people.end());
    
    // Ride Boat Big-one, Small-One
    while (nFrtOrd <= nBckOrd)
    {
        if (nFrtOrd == nBckOrd)
        {
            nNumBoat++;
            break;
        }
        
        // Sum Big + Small
        int nCarriage = people[nFrtOrd] + people[nBckOrd];
        
        // Over the limit then Ride Big-One
        if (nCarriage > MAX_WEIGHT)
        {
            nBckOrd--;
        }
        // Not over the limit then Ride both
        else
        {
            nFrtOrd++;
            nBckOrd--;
        }
        
        nNumBoat++;
    }
    
    answer = nNumBoat;
    
    return answer;
}
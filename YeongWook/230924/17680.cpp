/*****************************************
**  https://school.programmers.co.kr/learn/courses/30/lessons/17680
**  프로그래머스 코딩테스트 : 캐시
**  이 문제 및 풀이의 저작권은 프로그래머스에게 있습니다.
*****************************************/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string str_toupper(string str);

int solution(int cacheSize, vector<string> cities)
{
    int answer = 0;
    
    const int HIT = 1;
    const int MISS = 5;
    vector<string> cache;
    
    /* 캐시사이즈가 0이면 바로 리턴 */
    if (cacheSize == 0)
        return cities.size() * MISS;
    
    /* 도시이름 수 만큼 반복 */
    for (string city : cities)
    {
        /* 대소문자 구분을 위해 모든 도시 이름 전부 대문자로 변경 */
        city = str_toupper(city);
        
        /* 문자열 탐색 */
        auto hit = find(cache.begin(), cache.end(), city);
        
        /* 실행시간 기록 후 캐시메모리 갱신 */
        /* hit */
        if (hit != cache.end())
        {
            answer += HIT;
            cache.erase(hit);
            cache.push_back(city);
        }
        /* miss */
        else
        {
            answer += MISS;
            if (cache.size() == cacheSize)
                cache.erase(cache.begin());
            cache.push_back(city);
        }
    }
    
    return answer;
}


string str_toupper(string str)
{
    for (char& c : str)
    {
        if (c >= 'a' and c <= 'z')
            c -= 32;
    }
    return str;
}

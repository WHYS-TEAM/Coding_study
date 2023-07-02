#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    string tmpName = "";
    
    // 초기 이름 생성
    for (int i = 0; i < name.length(); i++) { tmpName += "A"; }
    
    // 이동
    int nIdx = 0;
    while(1)
    {
        int mvPt = min(name[nIdx] - 'A', 'Z' - name[nIdx]+1);

        answer += mvPt;
        
        tmpName[nIdx] = name[nIdx];
        
        if(tmpName == name) { return answer; }
        
        int rIdx = nIdx;
        int lIdx = nIdx;
        
        //오른쪽 이동 계산
        int rMvPt = 0;
        while(tmpName[rIdx] == name[rIdx])
        {
            rIdx++;
            rMvPt++;
            if(rIdx == name.length()) { rIdx = 0; }      
        }
        
        //왼쪽 이동 계산
        int lMvPt = 0;
        while(tmpName[lIdx] == name[lIdx])
        {
            lIdx--;
            lMvPt++;
            if(lIdx == -1) { lIdx = name.length()-1; }      
        }
        
        // 둘중 작은 값으로 이동
        if(lMvPt < rMvPt)
        {
            answer += lMvPt;
            nIdx = lIdx;
        }
        else
        {
            answer += rMvPt;
            nIdx = rIdx;
        }
    }
    
    return answer;
}
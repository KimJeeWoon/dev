import urllib3
import json
import sys
import requests

openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "d4a16891-dd45-4883-a873-777a8fda8787"
question = "한계성은 영어로 무엇입니까?"
passage = "  생명의 제가 생각하는 첫 속성은 한계성입니다. 모든 생명은 한정된 시간을 가지고 살아간다는 겁니다.영어로는 제가 이걸 ‘Ephemerality of Life’라고 표현을 하는데요. 조금 단어가 길고 어렵죠?Ephemerality가 어디에서 나오는 얘기냐 하면, 하루살이에서 나옵니다. 하루살이를 영어로 Ephemeroptera라고 합니다.우리가 왜 하루살이라고 부르느냐 하면, 하루살이는 유충으로 살 때는 물속에서 바위 밑에 기어 다니면서 사는데 몇 달이고 굉장히 오래 살거든요. 그런데 성충이 되고 난 다음에는 그저 하루 이틀 살면서 짝짓기하고 물에 알 낳고 죽어요.그래서 굉장히 짧은 인생을 우리가 흔히 ‘하루살이’라고 표현하는 거죠. 그래서 저도 한계성을 Ephemerality라고 표현하는 겁니다."
 
requestJson = {
"access_key": accessKey,
    "argument": {
        "question": question,
        "passage": passage
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")


data = json.loads(str(response.data,"utf-8")) 

sentence=data['return_object']['MRCInfo'] 
answer=sentence['answer']
confidence=sentence['confidence']
sys.stdout.write("Passage: "+passage)
print()
sys.stdout.write("Question: "+question)
print()
sys.stdout.write("Answer: "+answer) 
print()
sys.stdout.write("Confidence: "+confidence)
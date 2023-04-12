<h1> 주인님을 부탁해 </h1>

<h2>1. 프로젝트를 시작한 이유 : </h2>

<p>
    반려동물을 키우는 가구의 수는 꾸준히 증가하며 관련 산업 규모도 점차 커지고 있습니다.
    <br />
    하지만 아직까지 반려동물과 관련된 의료 분야들에는 미비한 점들이 다소 있다고 판단했습니다.
    <br />
    KB국민에서 발표한 2021년 한국반려동물보고서에 따르면 반려동물을 키우는 가구에서 지난 2년 평균 의료 지출 비용은 46만 5천원 입니다.
    <br />
    그 중 가장 높은 반려동물의 비중을 차지하는 강아지와 고양이의 의료 지출 내역은 피부병이 무려 약 40% 내외의 높은 비중을 차지하고 있습니다.
    <br />
    이러한 높은 비중을 차지하는 피부병을 조기에 발견하거나 예방할 수 있는 것을 목표로, 다소 동물병원에 자주 방문하기 어려운 직장인이나 학생들에게 보다 편리한 서비스를 제공하는 것을 목표로 프로젝트를 진행하였습니다.
</p> 
    <br />
<ul>
    <li>기술 스택 : flask (python)</li>
    <li>학습 모델 : Yolov5s</li>
    <li>데이터 출저 : <a href="https://aihub.or.kr/">AI Hub</a></li>
</ul>
    <br />

<h2>2. 해당 기술 사용 이유</h2>


<h3>flask</h3>
    <p>많은 기능들을 탑재해 다소 무거운 Django 보다는 가볍운 flask로 진행하여 필요한 기능들은 추후에 추가하는 방법으로 flask를 선택했습니다.</p>

<h3>yolov5</h3>
<p>이미지 학습을 하는 모델들 중에서 현재 프로젝트를 진행함에 있어서 가장 적합하다고 판단되어서 선택하게 되었습니다.</p>
<p>이유는 다음과 같습니다.</p>
<ul><li>현재 가지고 있는 자원적 한계(컴퓨터)가 오래 학습을 할 수 있거나 사양이 높지 못해, 구글 코랩을 사용해야하는 상황.</li>
    <li>구글 코랩은 24시간 내내 학습을 진행하도록 도와주지 않고 중간에 끊기는 경우가 다수 발생(끊기게 되면 학습했던 내용들이 전부 사라짐.)</li>
</ul>
그래서 가장 빠르게 학습이 되면서 학습하기 훨씬 용이한 Yolov5s를 선택했습니다.
<h3>데이터 전처리 및 학습</h3>
<p>Ai Hub에서 제공한 이미지 라벨링 데이터를 Yolov5에 맞춰서 데이터를 전처리하는 과정이 필요했습니다. <br/>
이에 다음과 같이 데이터를 전처리하는 과정을 진행했습니다.</p>
<p>yolov5는 라벨링을 하는 x,y의 기준이 일반적인 x1,y1,x2,y2와 다소 차이점을 볼 수 있습니다.<br/>
Ai Hub에서 제공하는 데이터 라벨은 x1,y1,x2,y2로 표시되어 있어서 이를 전처리하는 과정이 필요했습니다.</p>


<이미지 yolov5s>

```python 
import glob
import json

json_list = glob.glob("json/*.json")

for json_file in json_list:
    with open(json_file, "r", encoding="UTF-8") as f:
        data = json.load(f)
        
        width = "이미지 가로 사이즈"
        height = "이미지 세로 사이즈"

        for i in data['labelingInfo']:
            if 'box' in i.keys():

                label_x = i["box"]['location'][0]['x'] + \
                    i["box"]["location"][0]["width"] / 2
                label_x = label_x / width

                label_y = i['box']['location'][0]['y'] + \
                    i["box"]["location"][0]["height"] / 2
                label_y = label_y / height

                label_width = i["box"]["location"][0]["width"]/width
                label_height = i["box"]["location"][0]["height"]/height

                file_name = json_file.split('.')[0] + '.txt'
                with open(file_name, 'a', encoding='UTF-8') as f1:
                    f1.write(
                        f"5 {label_x} {label_y} {label_width} {label_height} \n")



```
<br/>

이렇게 데이터를 전처리한 커스텀 데이터는 아래의 공식문서를 참고하여 학습을 진행했습니다.

Yolov5 커스텀 학습<a href="https://docs.ultralytics.com/yolov5/train_custom_data/#environments"> GitHub</a>

<br/>

<h2>프로젝트 결과</h2>

<h3> 프로젝트 결과 : 모델 학습이 잘 안되서 아무것도 찾아내지 못하고 있다. </h3>
<p>그래서 yolov5s 에서 yolov5x로 변경을 해서 학습을 몇번 진행 하고 있지만 아직도 검증을 잘 못하고 있다.</p>
<p>계속 해서 여러 방법들을 통해서 학습을 진행해보려 하고 있다.</p>

<ul>
    <li> 메인 페이지
        <ul><li><img src="https://user-images.githubusercontent.com/113073492/231368198-2c33a55e-3321-41be-8261-66c0f959b1fb.png" /></li></ul>
    </li>
    <li> 검사 페이지
        <ul><li><img src="https://user-images.githubusercontent.com/113073492/231368197-12a7280c-2e61-4e8f-95d9-d19fad1d606a.png" /></li></ul>
    </li>
</ul>





<br/>
<hr/>
참고 자료
<ul>
    <li><a href="https://www.klnews.co.kr/news/articleView.html?idxno=305478">반려인 1,500만 시대, 떠오르는 먹거리 ‘반려동물 산업’</a></li>
    <li><a href="http://www.krei.re.kr/krei/selectBbsNttView.do?key=103&bbsNo=25&nttNo=125238&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=9&integrDeptCode=">[한국농촌경제연구원] 반려동물 연관 산업 확대, 문화·제도 뒷받침되어야</a></li>
    <li><a href="https://aihub.or.kr/">AI Hub</a></li>
    <li><a href="https://github.com/ultralytics/yolov5">yolov5s_Github</a></li>
    <li><a href="http://www.pet-news.or.kr/news/articleView.html?idxno=531">2022 펫코노미 시대를 넘어 ① 반려동물 관련 통계, 그 한계와 고민</a></li>
</ul>

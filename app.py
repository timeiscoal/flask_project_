from flask import Flask , render_template, request ,abort
from PIL import Image
import io
import base64
import torch

app = Flask(__name__, template_folder='templates', static_folder='static')

model = torch.hub.load("ultralytics/yolov5" , 'custom' , path='models_train/test1.pt', force_reload=True)

# request.args.get("")

@app.route('/')
def main():
    """ 메인 페이지 """
    return render_template("main.html")

@app.route('/test', methods=['GET', 'POST'])
def test_pages():
    """ 테스트 페이지 """

    if request.method == 'POST':
        image_input = request.files['file']
        if image_input != "":
            img_bytes = image_input.read()
            img_file = Image.open(io.BytesIO(img_bytes))
        
            result = model(img_file,size=640)

            result.ims
            result.render()
            for image in result.ims:
                buffered = io.BytesIO()
                img_base64 = Image.fromarray(image)
                img_base64.save(buffered, format="jpeg")
                encoded_img_data = base64.b64encode(buffered.getvalue()).decode("utf-8")
                return render_template('skin_result.html', img_data=encoded_img_data)
        
        else:
            abort(404)
    else:
        return render_template("skin_test.html")


@app.errorhandler(404)
def page_not_found(error):
    ''' 404 페이지 처리 '''
    return render_template("not_found_404.html"),404

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    if 'photo' not in request.files or 'prompt' not in request.form:
        return jsonify({'error': 'Missing photo or prompt'}), 400

    photo = request.files['photo']
    prompt = request.form['prompt']

    # Збереження фото (тимчасово)
    os.makedirs('tmp', exist_ok=True)
    photo_path = os.path.join('tmp', photo.filename)
    photo.save(photo_path)

    # Тут має бути логіка генерації відео — поки що повертаємо фейковий URL
    video_url = 'https://example.com/fake_video.mp4'

    return jsonify({
        'message': 'Video generated successfully',
        'video_url': video_url,
        'prompt_received': prompt
    })

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
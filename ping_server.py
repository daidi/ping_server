from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def get_ip():
    domain = request.args.get('domain', 'google.com')
    timeout = request.args.get('timeout', '2')  # 默认超时时间设置为2秒
    
    try:
        # 运行带超时参数的 ping 命令
        result = subprocess.run(
            ['ping', '-c', '1', '-W', timeout, domain],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return jsonify({'status': 'success', 'output': result.stdout}), 200
        else:
            return jsonify({'status': 'error', 'message': result.stderr}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#  baidu translatior : 1000 times/hour
import re, sys, urllib.request

def Translate(input, transl_from, transl_to):
	dict = {'chinese': 'zh', 'english': 'en'}
	
	try:
		q = urllib.parse.quote(input)
		urlBaiduTranslate =  'http://openapi.baidu.com/public/2.0/bmt/translate?client_id=4e5nLMnxIEkKVS5fTPvtMUYU&q=%s&from=%s&to=%s' % (q, dict[transl_from], dict[transl_to])
		
		data = urllib.request.urlopen(urlBaiduTranslate).read().decode('utf-8')
		regTxt = re.compile('(?<=\"dst\":\").*?(?=\"\}\])')
		output = regTxt.findall(data)[0]
		return output
		
	except Exception as e:
		print(e)
		return

if __name__ == "__main__":
	input = '这是一个测试用例'
	transl_from = 'chinese'
	transl_to = 'english'
	print(input)
	print(Translate(input, transl_from, transl_to))
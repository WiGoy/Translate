#  youdao translatior : 1000 times/hour
import re, sys, urllib.request

def Translate(input, transl_from, transl_to):
#	dict = {'chinese': 'zh', 'english': 'en'}
	
	try:
		q = urllib.parse.quote(input)
		urlYoudaoTranslate =  'http://fanyi.youdao.com/openapi.do?keyfrom=whoscored&key=654173872&type=data&doctype=json&version=1.1&only=translate&q=%s' % q
		
		data = urllib.request.urlopen(urlYoudaoTranslate).read().decode('utf-8')
		regTxt = re.compile('(?<=\"translation\":\[\").*?(?=\"\])')
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
#  google translatior
import re, urllib.request

def Translate(input, transl_from, transl_to):
	dict = {'chinese': 'zh-CN', 'english': 'en'}
	
	try:
		langpair = "\'%s\'|\'%s\'" % (dict[transl_from], dict[transl_to])
		urlGoTranslate = 'http://translate.google.cn/'
		params = urllib.parse.urlencode({'hl' : dict[transl_to], 'ie' : 'utf-8', 'text' : input, 'langpair' : langpair})
		browser = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		req = urllib.request.Request(url = urlGoTranslate, data = str.encode(params), headers = browser)
		
		page = urllib.request.urlopen(req)
		html = page.read().decode('utf-8')
		page.close()
		
		regTxt = re.compile('(?<=TRANSLATED_TEXT=\').*?(?=\';)')
		output = regTxt.findall(html)[0]
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
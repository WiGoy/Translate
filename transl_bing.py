#  bing translatior : 2,000,000 chars/month
import json, re, urllib.request

def GetAccessToken():
	clientID = 'WiGoy'
	clientSecret = 'YUHK8beVEyRMcVFuivskOcwJ3gUzlwzhtMiBhTVDBMk='
	grantType = 'client_credentials'
	scope = 'http://api.microsofttranslator.com'
	urlToken = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
	
	try:
		params = urllib.parse.urlencode({'client_id' : clientID, 'client_secret' : clientSecret, 'grant_type' : grantType, 'scope' : scope})
		req = urllib.request.Request(url = urlToken, data = str.encode(params))
		
		page = urllib.request.urlopen(req)
		html = page.read().decode('utf-8')
		page.close()
		
		access_token = json.loads(html)['access_token']
		return access_token
	
	except Exception as e:
		print(e)
		return

def Translate(input, transl_from, transl_to):
	dict = {'chinese': 'zh-CHS', 'english': 'en'}
	
	try:
		text = urllib.parse.quote(input)
		urlBingTranslate = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?text=%s&From=%s&To=%s' % (text, dict[transl_from], dict[transl_to])
		headers = {'Authorization' : 'Bearer %s' % GetAccessToken()}
		req = urllib.request.Request(url = urlBingTranslate, headers = headers)
		
		page = urllib.request.urlopen(req)
		html = page.read().decode('utf-8')
		page.close()
		
		regTxt = re.compile('(?<=\/\"\>).*?(?=<\/string\>)')
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
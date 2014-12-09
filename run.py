import time
import transl_baidu, transl_bing, transl_google, transl_youdao

if __name__ == "__main__":
#	input0 = '这是一个测试用例。我们会测试一条略微复杂的语句，看看哪个引擎的翻译质量比较好，并记录其翻译耗时。'
	input0 = '写了一个测试程序'
	transl_from = 'chinese'
	transl_to = 'english'
	
	print('input : %s\n' % input0)
	
	startTime = time.time()
	print('baidu : %s (%ss)\n' % (transl_baidu.Translate(input0, transl_from, transl_to), str(time.time() - startTime)))
	
	startTime = time.time()
	print('bing : %s (%ss)\n' % (transl_bing.Translate(input0, transl_from, transl_to), str(time.time() - startTime)))
	
	startTime = time.time()
	print('google : %s (%ss)\n' % (transl_google.Translate(input0, transl_from, transl_to), str(time.time() - startTime)))
	
	startTime = time.time()
	print('youdao : %s (%ss)\n' % (transl_youdao.Translate(input0, transl_from, transl_to), str(time.time() - startTime)))
mybooks = [{"제목":"안드로이드","저자":"최전산","출판사":"pbc","가격":2500,"출판년도":2017},
			{"제목":"안드로이드1","저자":"최전산1","출판사":"pbc1","가격":25000,"출판년도":20171}]

mybookslist = [["안드로이드","최전산","pbc",2500,2017],
["안드로이드1","최전산1","pbc1",25000,20171]]

#딕셔너리에서 출판사 출력
for onebook in mybooks:
	print(onebook["출판사"])

#리스트에서 출판사명 출력
for onebook in mybookslist:
	print(onebook[1])
"""
while True:
	choice = input('''도서 검색 키워드
	1. 도서명
	2. 저자명
	3. 출판사명
	4. 종료
	선택(1,2,3) : ''')
	if choice == '1' :#도서명
		kwd = "제목"
		#break
	elif choice =='2':#저자명
		kwd = "저자명"
		#break
	elif choice == '3': #출판사명
		kwd = "출판사"
		#break
	elif choice == '4':
		#loop = False
		break
	elif choice == '5':
		
	else:
		print("입력이 잘못되었습니다")
		
	userin = input(kwd + ">>>")
	find = False
	for onebook in mybooks:
		if userin == onebook[kwd]:
			print("제목:",onebook["제목"])
			print("저자", onebook["저자"])
			print("출판사", onebook["출판사"])
			print("가격", onebook["가격"])
			print("출판년도", onebook["출판년도"])
			
			find = True
			
	if find == False:
		print("검색한 도서가 없습니다")
"""

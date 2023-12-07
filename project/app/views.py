from django.shortcuts import render


def index(request):

	header = 'Данные пользователя'
	langs = ['Python', 'C', 'C++', 'C#', 'JavaSCript', 'Java']
	user = {'name': 'Abdulla', 'age': 18}
	address = ('Nichaevo', 14, 218)
	text = '<p>My text</p>'

	data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
	return render(request, 'index.html', context=data)

def contacts(request):
	return render(request, 'contacts.html')


def about(request):
	return render(request, 'about.html')
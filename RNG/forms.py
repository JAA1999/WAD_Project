from django import forms
from RNG.models import Users, Category, Game

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
							help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Category
		fields = ('name',)

class GameForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
							help_text="Please enter the title of the Game.") 
	url = forms.URLField(max_length=200,
						help_text="Please enter the URL of the Game.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Game
		exclude = ('category',)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length = 16, help_text="Create a username of a max 16 characters long.",required = True)
	password = forms.CharField(widget=forms.PasswordInput(),max_length = 32, help_text="Create a password of at least 8 characters long ",required=True)

	class Meta:
		model = Users
		fields = ("email", "username",  "password")

from django import forms


class regform(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)
    mobile = forms.IntegerField()
    address = forms.CharField(max_length=100)


class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


class shoplogform(forms.Form):
    email = forms.EmailField()
    code = forms.IntegerField()


class productform(forms.Form):
    name = forms.CharField(max_length=25)
    price = forms.IntegerField()
    image = forms.FileField()
    # desc = forms.CharField(max_length=50)


# class buyform(forms.Form):
#     name = forms.CharField(max_length=25)
#     price = forms.IntegerField()
#     quantity = forms.IntegerField()


class paymentform(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.CharField(max_length=20)
    fname = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    email = forms.EmailField()
    number = forms.IntegerField()
    paymode = forms.CharField(max_length=50)

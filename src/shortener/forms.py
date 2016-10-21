from django import forms


from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
            label='', 
            validators=[validate_url],
            widget = forms.TextInput(
                    attrs ={
                        "placeholder": "Long URL",
                        "class": "form-control"
                        }
                )
            )

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     return url
    #     #print(url)

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if "http" in url:
    #         return url
    #     return "http://" + url
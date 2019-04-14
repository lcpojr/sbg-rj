from django import forms


class OrderCreateForm(forms.Form):
    """
    A form to create a product order.
    """

    name = forms.CharField(label="Nome", required=True)
    email = forms.EmailField(label="Email", required=True)
    description = forms.CharField(label="Descrição", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Nome"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "E-mail"

        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Descreva aqui o(s) produto(s) que deseja comprar"


class ContactCreateForm(forms.Form):
    """
    A form to create a product order.
    """

    name = forms.CharField(label="Nome", required=True)
    email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Assunto", required=True)
    description = forms.CharField(label="Descrição", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactCreateForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Nome"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "E-mail"

        self.fields["subject"].widget.attrs["class"] = "form-control"
        self.fields["subject"].widget.attrs["placeholder"] = "Assunto"

        self.fields["description"].widget.attrs["class"] = "form-control"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Escreva aqui sua mensagem"

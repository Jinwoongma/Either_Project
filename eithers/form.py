from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    title = forms.CharField(
                max_length=50,
                label='제목',
                help_text='제목은 50자이내로 작성하세요.',
                required=True,
                widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '제목 입력',
                        }
                    )
            )

    selection1 = forms.CharField(
                max_length=50,
                label='답변 1',
                help_text='답변은 50자이내로 작성하세요.',
                required=True,
                widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '첫번째 답변 입력',
                        }
                    )
            )

    selection2 = forms.CharField(
                max_length=50,
                label='답변 2',
                help_text='답변은 50자이내로 작성하세요.',
                required=True,
                widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '두번째 답변 입력',
                        }
                    )
            )

    class Meta:
        model = Question
        fields = ['title', 'selection1', 'selection2']


class AnswerForm(forms.ModelForm):
    choices = [(0, 'left'), (1, 'right')]
    pick = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    class Meta:
        model = Answer
        fields = ['pick', 'comment']
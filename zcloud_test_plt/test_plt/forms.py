import ast
import json
from django import forms
from django.core.exceptions import ValidationError

from .models import ApiDef

FONT_MONO = 'font-family:monospace'


class RunApiForm(forms.Form):
    """
    执行接口-表单页
    """
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    query_params = forms.CharField(label='查询参数', required=False,
                                   widget=forms.Textarea(attrs={'rows': 6, 'cols': 80, 'style': FONT_MONO}))
    http_headers = forms.CharField(label='请求头', required=False,
                                   widget=forms.Textarea(attrs={'rows': 6, 'cols': 80, 'style': FONT_MONO}))
    request_body = forms.CharField(label='请求体', required=False,
                                   widget=forms.Textarea(attrs={'rows': 6, 'cols': 80, 'style': FONT_MONO}))
    auth_username = forms.CharField(label='Basic认证用户名', required=False)
    auth_password = forms.CharField(label='Basic认证密码', required=False)
    bearer_token = forms.CharField(label='Bearer认证令牌', required=False,
                                   widget=forms.Textarea(attrs={'rows': 6, 'cols': 80}))

    def clean_request_body(self):
        """
        解析请求体为Json或普通文本
        :param self:
        :return:普通文本或字典
        """
        val = self.cleaned_data.get("request_body")

        if not val:
            return val
        api = self.get_apidef()
        if api.body_type in ('form-urlencoded', 'raw-json'):
            return self.chk_json('request_body')
        else:
            return val

    def clean_query_params(self):
        """
        处理查询参数数据校验
        :return:
        """
        return self.chk_json('query_params')

    def clean_http_headers(self):
        """
        处理请求头数据校验
        :return:
        """
        val = self.chk_json('http_headers')
        if not val.isascii():
            raise ValidationError('HTTP Header 只支持ASCII字符！')
        return val

    def clean_request_body(self):
        """
        处理请求体数据检验
        :return:
        """
        val = self.cleaned_data.get("request_body")

        if not val:
            return val
        api = self.get_apidef()
        if api.body_type in ('form-urlencoded', 'raw-json'):
            return self.chk_json('request_body')
        else:
            return val

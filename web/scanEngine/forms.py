from django import forms
from scanEngine.models import *
from django_ace import AceWidget
from reNgine.validators import validate_short_name


class AddEngineForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = '__all__'
    engine_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "scan_engine_name",
                "placeholder": "Custom Engine"}))
    subdomain_discovery = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"checked": ""}))
    screenshot = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"checked": ""}))
    dir_file_search = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={}))
    port_scan = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={}))
    fetch_url = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"checked": ""}))
    vulnerability_scan = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"checked": ""}))
    osint = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"checked": ""}))
    yaml_configuration = forms.CharField(widget=AceWidget(
        mode="yaml",
        theme="monokai",
        width="100%",
        height="450px",
        tabsize=4,
        fontsize=13,
        toolbar=True,
        attrs={"id": "editor", "value": "ok"}))


class UpdateEngineForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = '__all__'
    engine_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "scan_engine_name",
                "placeholder": "Custom Engine"}))
    subdomain_discovery = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    screenshot = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    dir_file_search = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    port_scan = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    fetch_url = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    vulnerability_scan = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    osint = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput())
    yaml_configuration = forms.CharField(widget=AceWidget(
        mode="yaml",
        theme="monokai",
        width="100%",
        height="450px",
        tabsize=4,
        fontsize=13,
        toolbar=True,))

    def set_value(self, engine):
        self.initial['engine_name'] = engine.engine_name
        self.initial['subdomain_discovery'] = engine.subdomain_discovery
        self.initial['dir_file_search'] = engine.dir_file_search
        self.initial['port_scan'] = engine.port_scan
        self.initial['fetch_url'] = engine.fetch_url
        self.initial['yaml_configuration'] = engine.yaml_configuration
        self.initial['vulnerability_scan'] = engine.vulnerability_scan
        self.initial['osint'] = engine.osint
        self.initial['screenshot'] = engine.screenshot


class AddWordlistForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'name',
                   'placeholder': 'my awesome wordlist', }))
    short_name = forms.CharField(
        required=True,
        validators=[validate_short_name],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'short_name',
                'placeholder': 'my_awesome_wordlist', }))
    upload_file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={'class': 'custom-file-input',
                   'id': 'txtFile',
                   'multiple': '',
                   'accept': '.txt', }))


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = '__all__'
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'name',
                   'placeholder': 'Configuration Name', }))
    short_name = forms.CharField(
        required=True,
        validators=[validate_short_name],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'short_name',
                'placeholder': 'my_awesome_configuration', }))
    content = forms.CharField(widget=AceWidget(
        mode="text",
        theme="monokai",
        width="100%",
        height="450px",
        tabsize=4,
        fontsize=13,
        toolbar=True,))

    def set_value(self, configuration):
        self.initial['name'] = configuration.name
        self.initial['short_name'] = configuration.short_name
        self.initial['content'] = configuration.content


class InterestingLookupForm(forms.ModelForm):
    class Meta:
        model = InterestingLookupModel
        fields = '__all__'
    keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "keywords",
                "placeholder": "Interesting Keywords",
            }))

    custom_type = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(
            attrs={
                "value": 'true'
                }))

    title_lookup = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
            }))

    url_lookup = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
            }))

    condition_200_http_lookup = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
            }))

    def set_value(self, key):
        print(key.url_lookup)
        self.initial['keywords'] = key.keywords
        self.initial['title_lookup'] = key.title_lookup
        self.initial['url_lookup'] = key.url_lookup
        self.initial['condition_200_http_lookup'] = key.condition_200_http_lookup

    def initial_checkbox(self):
        self.initial['title_lookup'] = True
        self.initial['url_lookup'] = True
        self.initial['condition_200_http_lookup'] = False


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

    send_to_slack = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "slack_checkbox",
            }))

    slack_hook_url = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "slack_hook_url",
                "placeholder": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
            }))

    send_to_discord = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "discord_checkbox",
            }))

    discord_hook_url = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "discord_hook_url",
                "placeholder": "https://discord.com/api/webhooks/000000000000000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            }))

    send_to_telegram = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "telegram_checkbox",
            }))

    telegram_bot_token = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "telegram_bot_token",
                "placeholder": "Bot Token",
            }))

    telegram_bot_chat_id = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "telegram_bot_chat_id",
                "placeholder": "Bot Chat ID",
            }))

    send_scan_status_notif = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "custom-control-input",
                "id": "send_scan_status_notif",
            }))

    send_interesting_notif = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "custom-control-input",
                "id": "send_interesting_notif",
            }))


    send_vuln_notif = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "custom-control-input",
                "id": "send_vuln_notif",
            }))


    send_subdomain_changes_notif = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "custom-control-input",
                "id": "send_subdomain_changes_notif",
            }))


    send_scan_output_file = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "custom-control-input",
                "id": "send_scan_output_file",
            }))


    def set_value(self, key):
        self.initial['send_to_slack'] = key.send_to_slack
        self.initial['send_to_discord'] = key.send_to_discord
        self.initial['send_to_telegram'] = key.send_to_telegram

        self.initial['slack_hook_url'] = key.slack_hook_url
        self.initial['discord_hook_url'] = key.discord_hook_url
        self.initial['telegram_bot_token'] = key.telegram_bot_token
        self.initial['telegram_bot_chat_id'] = key.telegram_bot_chat_id

        self.initial['send_scan_status_notif'] = key.send_scan_status_notif
        self.initial['send_interesting_notif'] = key.send_interesting_notif
        self.initial['send_vuln_notif'] = key.send_vuln_notif
        self.initial['send_subdomain_changes_notif'] = key.send_subdomain_changes_notif

        self.initial['send_scan_output_file'] = key.send_scan_output_file

        if not key.send_to_slack:
            self.fields['slack_hook_url'].widget.attrs['readonly'] = True
        if not key.send_to_discord:
            self.fields['discord_hook_url'].widget.attrs['readonly'] = True
        if not key.send_to_telegram:
            self.fields['telegram_bot_token'].widget.attrs['readonly'] = True
            self.fields['telegram_bot_chat_id'].widget.attrs['readonly'] = True


    def set_initial(self):
        self.initial['send_to_slack'] = False
        self.initial['send_to_discord'] = False
        self.initial['send_to_telegram'] = False

        self.fields['slack_hook_url'].widget.attrs['readonly'] = True
        self.fields['discord_hook_url'].widget.attrs['readonly'] = True
        self.fields['telegram_bot_token'].widget.attrs['readonly'] = True
        self.fields['telegram_bot_chat_id'].widget.attrs['readonly'] = True

        self.initial['send_scan_status_notif'] = True
        self.initial['send_interesting_notif'] = True
        self.initial['send_vuln_notif'] = True
        self.initial['send_subdomain_changes_notif'] = True

        self.initial['send_scan_output_file'] = True


class ProxyForm(forms.ModelForm):
    class Meta:
        model = Proxy
        fields = '__all__'

    use_proxy = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "use_proxy",
            }))

    proxies = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "proxies",
                "rows": "10",
                "spellcheck": "false",
                "placeholder": "http://username:password@proxyip.com:port",
            }))

    def set_value(self, key):
        self.initial['use_proxy'] = key.use_proxy
        self.initial['proxies'] = key.proxies

        if not key.use_proxy:
            self.fields['proxies'].widget.attrs['readonly'] = True

    def set_initial(self):
        self.initial['use_proxy'] = False
        self.fields['proxies'].widget.attrs['readonly'] = True


class HackeroneForm(forms.ModelForm):
    class Meta:
        model = Hackerone
        fields = '__all__'

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Your Hackerone Username",
            }))

    api_key = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "api_key",
                "placeholder": "Hackerone API Token",
            }))

    send_critical = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "send_critical",
            }))

    send_high = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "send_high",
            }))

    send_medium = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "send_medium",
            }))

    report_template = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "vulnerability-report-template"
            }))

    def set_value(self, key):
        self.initial['username'] = key.username
        self.initial['api_key'] = key.api_key

        self.initial['send_critical'] = key.send_critical
        self.initial['send_high'] = key.send_high
        self.initial['send_medium'] = key.send_medium

        self.initial['report_template'] = key.report_template

    def set_initial(self):
        self.initial['send_critical'] = True
        self.initial['send_high'] = True
        self.initial['send_medium'] = False

        self.initial['report_template'] = '''Hi Team, while testing, a {vulnerability_severity} severity vulnerability has been discovered in {vulnerable_url} and below is the findings.

# Vulnerability
{vulnerability_name}

## Issue Description
{vulnerability_description}

## Vulnerable URL
- {vulnerable_url}

## Extracted Results/Findings
{vulnerability_extracted_results}

## References
- {vulnerability_reference}

Thank you'''


class ReportForm(forms.ModelForm):
    class Meta:
        model = VulnerabilityReportSettings
        fields = '__all__'

    company_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "company_name",
                "placeholder": "Company Name",
            }))

    company_address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "company_address",
                "placeholder": "Company Address",
            }))

    company_website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "company_website",
                "placeholder": "Company Website https://company.com",
            }))

    company_email = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "company_email",
                "placeholder": "email@yourcompany.com",
            }))

    show_footer = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "show_footer",
            }))

    footer_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "footer_text",
            "aria-label": "switch",
            "placeholder": "Footer Text © Your Company",
        }))

    show_rengine_banner = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "show_rengine_banner",
            }))

    show_executive_summary = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "new-control-input",
                "id": "show_executive_summary",
            }))

    executive_summary_description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "executive_summary_description"
            }))

    def set_value(self, key):
        self.initial['company_name'] = key.company_name
        self.initial['company_address'] = key.company_address
        self.initial['company_website'] = key.company_website
        self.initial['company_email'] = key.company_email
        self.initial['show_rengine_banner'] = key.show_rengine_banner
        self.initial['show_executive_summary'] = key.show_executive_summary
        self.initial['executive_summary_description'] = key.executive_summary_description
        self.initial['show_footer'] = key.show_footer
        self.initial['footer_text'] = key.footer_text

    def set_initial(self):
        self.initial['show_rengine_banner'] = True
        self.initial['show_footer'] = False
        self.initial['show_executive_summary'] = False
        self.initial['executive_summary_description'] = '''On **{scan_date}**, **{target_name}** engaged **{company_name}** to perform a security audit on their Web application.

**{company_name}** performed both Security Audit and Reconnaissance using automated tool reNgine. https://github.com/yogeshojha/rengine .

## Observations

During the course of this engagement **{company_name}** was able to discover **{subdomain_count}** Subdomains and  **{vulnerability_count}** Vulnerabilities, including informational vulnerabilities and these could pose a significant risk to the security of the application.

The breakdown of the Vulnerabilities Identified in **{target_name}** by severity are as follows:

* Critical : {critical_count}
* High : {high_count}
* Medium : {medium_count}
* Low : {low_count}
* Info : {info_count}

**{company_name}** recommends that these issues be addressed in timely manner.

'''

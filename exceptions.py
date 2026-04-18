class ScriptError(Exception):
    pass

class ConfigurationError(ScriptError):
    pass

class EmailParsingError(ScriptError):
    pass

class AutomationError(ScriptError):
    pass

class CaptchaApiError(ScriptError):
    pass
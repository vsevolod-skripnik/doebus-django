from rest_framework.throttling import AnonRateThrottle

from app.base.api.throttling import ConfigurableThrottlingMixin


class AuthAnonRateThrottle(ConfigurableThrottlingMixin, AnonRateThrottle):
    """Throttle for any authorization views."""
    scope = 'anon-auth'

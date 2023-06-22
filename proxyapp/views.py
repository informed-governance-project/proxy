from revproxy.views import ProxyView

from proxy.models import ExternalToken


class DefaultProxyView(ProxyView):
    # upstream = "http://127.0.0.1:5000/"

    def get_proxy_request_headers(self, request):
        # print(self.upstream)
        # print(request.user)
        headers = super().get_proxy_request_headers(request)

        module_path = request.path.strip("/")
        try:
            external_token = ExternalToken.objects.get(
                user=request.user, module_path=module_path
            )
        except ExternalToken.DoesNotExist:
            # return the headers without the authentication token
            return headers

        headers["token"] = external_token.token
        return headers

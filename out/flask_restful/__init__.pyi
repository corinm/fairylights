from flask.views import MethodView
from typing import Any, Optional

def abort(http_status_code: Any, **kwargs: Any) -> None: ...

class Api:
    representations: Any = ...
    urls: Any = ...
    prefix: Any = ...
    default_mediatype: Any = ...
    decorators: Any = ...
    catch_all_404s: Any = ...
    serve_challenge_on_401: Any = ...
    url_part_order: Any = ...
    errors: Any = ...
    blueprint_setup: Any = ...
    endpoints: Any = ...
    resources: Any = ...
    app: Any = ...
    blueprint: Any = ...
    def __init__(self, app: Optional[Any] = ..., prefix: str = ..., default_mediatype: str = ..., decorators: Optional[Any] = ..., catch_all_404s: bool = ..., serve_challenge_on_401: bool = ..., url_part_order: str = ..., errors: Optional[Any] = ...) -> None: ...
    def init_app(self, app: Any) -> None: ...
    def owns_endpoint(self, endpoint: Any): ...
    def error_router(self, original_handler: Any, e: Any): ...
    def handle_error(self, e: Any): ...
    def mediatypes_method(self): ...
    def add_resource(self, resource: Any, *urls: Any, **kwargs: Any) -> None: ...
    def resource(self, *urls: Any, **kwargs: Any): ...
    def output(self, resource: Any): ...
    def url_for(self, resource: Any, **values: Any): ...
    def make_response(self, data: Any, *args: Any, **kwargs: Any): ...
    def mediatypes(self): ...
    def representation(self, mediatype: Any): ...
    def unauthorized(self, response: Any): ...

class Resource(MethodView):
    representations: Any = ...
    method_decorators: Any = ...
    def dispatch_request(self, *args: Any, **kwargs: Any): ...

def marshal(data: Any, fields: Any, envelope: Optional[Any] = ...): ...

class marshal_with:
    fields: Any = ...
    envelope: Any = ...
    def __init__(self, fields: Any, envelope: Optional[Any] = ...) -> None: ...
    def __call__(self, f: Any): ...

class marshal_with_field:
    field: Any = ...
    def __init__(self, field: Any) -> None: ...
    def __call__(self, f: Any): ...

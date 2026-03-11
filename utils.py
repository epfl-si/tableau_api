import tableauserverclient as TSC
from json import dumps
from typing import Any, Dict
from jwt import encode
from datetime import datetime, timezone, timedelta
from uuid import uuid4


def generate_jwt(connected_app_client_id, connected_app_secret_id, connected_app_secret_value, username):
    payload = {
        "iss": connected_app_client_id,
        "sub": username,
        "aud": "tableau",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=10),
        "jti": str(uuid4()),
        "scp": ["tableau:viz_data_service:read"],
    }
    return encode(payload=payload,key=connected_app_secret_value,
        algorithm="HS256",
        headers={"kid": connected_app_secret_id},
    )


def obj_to_dict(obj: Any) -> Dict[str, Any]:
    ds_dict = {}
    attributes = [a for a in dir(obj) if not a.startswith('_')]
    for attr in attributes:
        try:
            value = getattr(obj, attr)
            if value is None:
                continue
        except TSC.models.exceptions.UnpopulatedPropertyError:
            continue
        if is_jsonable(value):
            ds_dict[attr] = value
        elif isinstance(value, datetime):
            ds_dict[attr] = value.isoformat()
        elif callable(value):
            continue
        else:
            for sub_attr in ('id', 'name', 'fullname'):
                if hasattr(value, sub_attr) and f'{attr}_{sub_attr}' not in attributes:
                    sub_value = getattr(value, sub_attr)
                    if sub_value is not None:
                        ds_dict[f'{attr}_{sub_attr}'] = getattr(value, sub_attr)
    return ds_dict


def is_jsonable(x):
    try:
        dumps(x)
        return True
    except (TypeError, OverflowError):
        return False


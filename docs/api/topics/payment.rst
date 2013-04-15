.. _payment:

========
Payments
========

This API is specific to setting up and processing payments for an app in the
Marketplace.

Installing
==========

When an app is installed from the Marketplace, call the install API. This will
record the install. If the app is a paid app, it will return the receipt that
to be used on install.

.. http:post:: /api/v1/receipts/install/

    Returns a receipt if the app is paid and a receipt should be installed.

    **Request**:

    .. sourcecode:: http

        POST /api/v1/receipts/install/

    :param app: the id of the app being installed.

    **Response**:

    .. code-block:: http

        {"receipt": "ey...[truncated]"}

    :statuscode 201: successfully completed.
    :statuscode 402: payment required.
    :statuscode 403: app is not public, install not allowed.

Developers
~~~~~~~~~~

Developers of the app will get a special developer receipt that is valid for
24 hours and does not require payment.

Reviewers
~~~~~~~~~

Reviewers should not use this API.

Pay Tiers
==========

.. note:: Accessible via CORS_.

.. http:get:: /api/v1/webpay/prices/

    Gets a list of pay tiers from the Marketplace.

    **Request**

    :param provider: (optional) the payment provider. Current values: *bango*

    The standard :ref:`list-query-params-label`.

    **Response**

    :param meta: :ref:`meta-response-label`.
    :param objects: A :ref:`listing <objects-response-label>` of :ref:`apps <pay-tier-response-label>`.
    :statuscode 200: successfully completed.

.. _pay-tier-response-label:

.. http:get:: /api/v1/webpay/prices/(int:id)/

    **Response**

    .. code-block:: json

        {
            "name": "Tier 1",
            "prices": [{
                "amount": "0.99",
                "currency": "USD"
            }, {
                "amount": "0.69",
                "currency": "GBP"
            }],
            "localized": {},
            "resource_uri": "/api/v1/webpay/prices/1/"
        }

    :param localized: see `Localized tier`.
    :statuscode 200: successfully completed.


Localized tier
~~~~~~~~~~~~~~

To display a price to your user, it would be nice to know how to display a
price in the app. The Marketplace does some basic work to calculate the locale
of a user. Information that would be useful to show to your user is placed in
the localized field of the result.

A request with the HTTP *Accept-Language* header set to *pt-BR*, means that
*localized* will contain:

    .. code-block:: json

        {
            "localized": {
                "amount": "10.00",
                "currency": "BRL",
                "locale": "R$10,00",
                "region": "Brasil"
            }
        }

The exact same request with an *Accept-Language* header set to *en-US*
returns:

    .. code-block:: json

        {
            "localized": {
                "amount": "0.99",
                "currency": "USD",
                "locale": "$0.99",
                "region": "United States"
            }
        }

If a suitable currency for the region given in the request cannot be found, the
result will be empty. It could be that the currency that the Marketplace will
accept is not the currency of the country. For example, a request with
*Accept-Language* set to *fr* may result in:

    .. code-block:: json

        {
            "localized": {
                "amount": "1.00",
                "currency": "USD",
                "locale": "1,00\xa0$US",
                "region": "Monde entier"
            }
        }

Please note: these are just examples to demonstrate cases. Actual results will
vary depending upon data sent and payment methods in the Marketplace.

.. _CORS: https://developer.mozilla.org/en-US/docs/HTTP/Access_control_CORS

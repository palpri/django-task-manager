from rest_framework.views import exception_handler

def global_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Customize response format
        response.data = {
            "error": response.data.get('detail', str(exc))
        }
    else:
        # fallback for exceptions not handled by DRF
        from rest_framework.response import Response
        from rest_framework import status
        response = Response({"error": str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response

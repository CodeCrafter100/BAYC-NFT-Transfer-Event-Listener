from django.http import JsonResponse
from event_listener.models import TransferEvent

def transfer_history(request, token_id):
    events = TransferEvent.objects.filter(token_id=token_id)
    
    if not events.exists():
        return JsonResponse({"message": "No transfers found for this token ID"}, status=404)


    response_data = [
        {
            'token_id': event.token_id,
            'from_address': event.from_address,
            'to_address': event.to_address,
            'transaction_hash': event.transaction_hash,
            'block_number': event.block_number
        }
        for event in events
    ]

    return JsonResponse(response_data, safe=False)

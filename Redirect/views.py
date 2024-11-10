from django.shortcuts import redirect, render, get_object_or_404
from .models import Referral

def redirect_view(request):
    ref_code = request.GET.get('ref')
    referral = get_object_or_404(Referral, code=ref_code)
    return redirect(f"{referral.redirect_url}?ref={ref_code}")

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from apps.accounts.views import accept_staff_invitation, jurisdiction_setup, login_view, mfa_setup, mfa_verify, my_account, secure_logout
from apps.web.api import deadline_list_api
from apps.web.deadline_create_api import deadline_create_api
from apps.web.deadline_options_api import deadline_options_api
from apps.web.deadline_preview_api import deadline_preview_api
from apps.web.matter_actions import add_deadline_api, add_event_api, add_party_api, deadline_status_api
from apps.web.matter_api import matter_assignments_api, matter_detail_api, matters_api
from apps.web.views import administration_page, dashboard, deadlines_page, events_page, landing_page, matter_workspace, matters_page, parties_page, privacy_page, robots_txt, sitemap_xml, terms_page


def health(request):
    return JsonResponse({"status": "ok", "service": "formata-3"})


urlpatterns = [
    path("", landing_page, name="home"),
    path("terms/", terms_page, name="terms"),
    path("privacy/", privacy_page, name="privacy"),
    path("robots.txt", robots_txt, name="robots"),
    path("sitemap.xml", sitemap_xml, name="sitemap"),
    path("dashboard/", dashboard, name="dashboard"),
    path("matters/", matters_page, name="matters"),
    path("matters/<uuid:matter_id>/", matter_workspace, name="matter-workspace"),
    path("deadlines/", deadlines_page, name="deadlines"),
    path("parties/", parties_page, name="parties"),
    path("events/", events_page, name="events"),
    path("administration/", administration_page, name="administration"),
    path("api/matters/", matters_api, name="matters-api"),
    path("api/matters/<uuid:matter_id>/", matter_detail_api, name="matter-detail-api"),
    path("api/matters/<uuid:matter_id>/assignments/", matter_assignments_api, name="matter-assignments-api"),
    path("api/matters/<uuid:matter_id>/parties/", add_party_api, name="matter-add-party-api"),
    path("api/matters/<uuid:matter_id>/events/", add_event_api, name="matter-add-event-api"),
    path("api/matters/<uuid:matter_id>/deadlines/", add_deadline_api, name="matter-add-deadline-api"),
    path("api/deadlines/", deadline_list_api, name="deadline-list-api"),
    path("api/deadlines/create/", deadline_create_api, name="deadline-create-api"),
    path("api/deadlines/options/", deadline_options_api, name="deadline-options-api"),
    path("api/deadlines/preview/", deadline_preview_api, name="deadline-preview-api"),
    path("api/deadlines/<uuid:deadline_id>/status/", deadline_status_api, name="deadline-status-api"),
    path("accounts/login/", login_view, name="login"),
    path("accounts/invitations/<str:token>/", accept_staff_invitation, name="accept-staff-invitation"),
    ##!! theres a world this can leak the token in browser or logs 
    path("accounts/jurisdiction/", jurisdiction_setup, name="jurisdiction-setup"),
    path("accounts/me/", my_account, name="my-account"),
    path("accounts/mfa/setup/", mfa_setup, name="mfa-setup"),
    path("accounts/mfa/verify/", mfa_verify, name="mfa-verify"),
    path("accounts/logout/", secure_logout, name="logout"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
]

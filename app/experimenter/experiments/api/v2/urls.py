from django.conf.urls import url

from experimenter.experiments.api.v2.views import (
    ExperimentCloneView,
    ExperimentCSVListView,
    ExperimentDesignAddonRolloutView,
    ExperimentDesignAddonView,
    ExperimentDesignBranchedAddonView,
    ExperimentDesignGenericView,
    ExperimentDesignMessageView,
    ExperimentDesignMultiPrefView,
    ExperimentDesignPrefRolloutView,
    ExperimentDesignPrefView,
    ExperimentSendIntentToShipEmailView,
    ExperimentTimelinePopulationView,
)


urlpatterns = [
    url(r"^csv/$", ExperimentCSVListView.as_view(), name="experiments-api-csv",),
    url(
        r"^(?P<slug>[\w-]+)/intent-to-ship-email$",
        ExperimentSendIntentToShipEmailView.as_view(),
        name="experiments-api-send-intent-to-ship-email",
    ),
    url(
        r"^(?P<slug>[\w-]+)/clone",
        ExperimentCloneView.as_view(),
        name="experiments-api-clone",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-addon-rollout",
        ExperimentDesignAddonRolloutView.as_view(),
        name="experiments-design-pref-rollout",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-addon",
        ExperimentDesignAddonView.as_view(),
        name="experiments-design-addon",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-pref-rollout",
        ExperimentDesignPrefRolloutView.as_view(),
        name="experiments-design-addon-rollout",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-pref",
        ExperimentDesignPrefView.as_view(),
        name="experiments-design-pref",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-multi-pref",
        ExperimentDesignMultiPrefView.as_view(),
        name="experiments-design-multi-pref",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-generic",
        ExperimentDesignGenericView.as_view(),
        name="experiments-design-generic",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-branched-addon",
        ExperimentDesignBranchedAddonView.as_view(),
        name="experiments-design-branched-addon",
    ),
    url(
        r"^(?P<slug>[\w-]+)/design-message",
        ExperimentDesignMessageView.as_view(),
        name="experiments-design-message",
    ),
    url(
        r"^(?P<slug>[\w-]+)/timeline-population",
        ExperimentTimelinePopulationView.as_view(),
        name="experiments-timeline-population",
    ),
]

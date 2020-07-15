from rest_framework.generics import (
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework_csv.renderers import CSVRenderer


from experimenter.experiments.constants import ExperimentConstants
from experimenter.experiments.models import Experiment
from experimenter.experiments import email
from experimenter.experiments.filtersets import ExperimentFilterset
from experimenter.experiments.api.v1.serializers import ExperimentSerializer
from experimenter.experiments.api.v2.serializers import (
    ExperimentCloneSerializer,
    ExperimentDesignAddonRolloutSerializer,
    ExperimentDesignAddonSerializer,
    ExperimentDesignBranchedAddonSerializer,
    ExperimentDesignGenericSerializer,
    ExperimentDesignMessageSerializer,
    ExperimentDesignMultiPrefSerializer,
    ExperimentDesignPrefRolloutSerializer,
    ExperimentDesignPrefSerializer,
    ExperimentTimelinePopSerializer,
    ExperimentCSVSerializer,
)


class ExperimentSendIntentToShipEmailView(UpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(status=Experiment.STATUS_REVIEW)
    serializer_class = ExperimentSerializer

    def update(self, request, *args, **kwargs):
        experiment = self.get_object()

        if experiment.review_intent_to_ship:
            return Response(
                {"error": "email-already-sent"}, status=status.HTTP_409_CONFLICT
            )

        email.send_intent_to_ship_email(experiment.id)

        experiment.review_intent_to_ship = True
        experiment.save()

        return Response()


class ExperimentCloneView(UpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.all()
    serializer_class = ExperimentCloneSerializer


class ExperimentDesignPrefView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_PREF)
    serializer_class = ExperimentDesignPrefSerializer


class ExperimentDesignMultiPrefView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_PREF)
    serializer_class = ExperimentDesignMultiPrefSerializer


class ExperimentDesignAddonView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_ADDON)
    serializer_class = ExperimentDesignAddonSerializer


class ExperimentDesignGenericView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_GENERIC)
    serializer_class = ExperimentDesignGenericSerializer


class ExperimentDesignBranchedAddonView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_ADDON)
    serializer_class = ExperimentDesignBranchedAddonSerializer


class ExperimentDesignPrefRolloutView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_ROLLOUT)
    serializer_class = ExperimentDesignPrefRolloutSerializer


class ExperimentDesignAddonRolloutView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_ROLLOUT)
    serializer_class = ExperimentDesignAddonRolloutSerializer


class ExperimentDesignMessageView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.filter(type=ExperimentConstants.TYPE_MESSAGE)
    serializer_class = ExperimentDesignMessageSerializer


class ExperimentTimelinePopulationView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Experiment.objects.all()
    serializer_class = ExperimentTimelinePopSerializer


class ExperimentCSVListView(ListAPIView):
    queryset = Experiment.objects.get_prefetched().order_by("status", "name")
    serializer_class = ExperimentCSVSerializer
    renderer_classes = (CSVRenderer,)

    def get_queryset(self):
        return ExperimentFilterset(
            self.request.GET, super().get_queryset(), request=self.request
        ).qs

    def get_renderer_context(self):
        # Pass the ordered list of fields in to specify the ordering of the headers
        # otherwise it defaults to sorting them alphabetically
        context = super().get_renderer_context()
        context["header"] = self.serializer_class.Meta.fields
        return context

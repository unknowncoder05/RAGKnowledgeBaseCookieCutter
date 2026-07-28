from django.conf import settings
from django.db import models


class KnowledgeSource(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class KnowledgeDocument(models.Model):
    class Status(models.TextChoices):
        UPLOADED = "uploaded", "Uploaded"
        INGESTING = "ingesting", "Ingesting"
        READY = "ready", "Ready"
        FAILED = "failed", "Failed"

    source = models.ForeignKey(KnowledgeSource, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    status = models.CharField(max_length=24, choices=Status.choices, default=Status.UPLOADED)
    storage_uri = models.TextField(blank=True, default="")
    content_type = models.CharField(max_length=120, blank=True, default="")
    checksum = models.CharField(max_length=128, blank=True, default="")
    error_message = models.TextField(blank=True, default="")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class KnowledgeChunk(models.Model):
    document = models.ForeignKey(KnowledgeDocument, related_name="chunks", on_delete=models.CASCADE)
    ordinal = models.PositiveIntegerField()
    text = models.TextField()
    token_count = models.PositiveIntegerField(default=0)
    citation = models.JSONField(default=dict, blank=True)
    embedding_model = models.CharField(max_length=120, blank=True, default="")
    embedding = models.JSONField(default=list, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["document_id", "ordinal"]
        unique_together = ("document", "ordinal")

    def __str__(self):
        return f"{self.document_id}:{self.ordinal}"

from django.db import models

from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


def generate_reference_number():
    """
    Generates a unique reference number based on a fixed prefix and a sequential counter.
    """
    prefix = "ICT-"
    counter = Document.objects.count() + 1  # Get existing document count and increment
    return f"{prefix}{counter:03d}"  # Format as ICT-001 (3-digit counter)


class Document(models.Model):
    """
    Represents a document within the system, with detailed fields and relationships.
    """

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("under_review", "Under Review"),
        ("approved", "Approved"),
    )

    ref_number = models.CharField(
        max_length=255,
        unique=True,
        help_text="Unique reference number for the document.",
    )
    document_name = models.CharField(max_length=255, help_text="Name of the document.")
    document_description = models.TextField(
        blank=True, help_text="Optional description of the document's content."
    )
    approval_date = models.DateField(
        blank=True, null=True, help_text="Date the document was approved."
    )
    council_resolution_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Council resolution number associated with the document.",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        help_text="Status of the document.",
    )

    created_at = models.DateTimeField(
        default=timezone.now, help_text="Timestamp when the document was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when the document was last updated."
    )

    document_file = models.FileField(
        upload_to="documents/",
        default="",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        help_text="Upload the document file.",
    )

    def save(self, *args, **kwargs):
        if not self.ref_number:
            self.ref_number = generate_reference_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ref_number + " - " + self.document_name

    class Meta:
        ordering = [
            "-created_at"
        ]  # Order documents by their creation date in descending order

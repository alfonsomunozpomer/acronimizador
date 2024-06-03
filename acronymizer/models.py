from django.db import models

# The longest word in Spanish is "Electroencefalografista" with 23 characters
class Submission(models.Model):
    status_choices = {
        'P': 'Pending',
        'A': 'Approved',
        'R': 'Rejected'
    }

    word = models.CharField(max_length=25)
    sent_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=status_choices, default='P') 
    updated_date = models.DateTimeField(null=True)

class AcronymToken(models.Model):
    prepositions = {'a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras'}
    preposition_choices = {preposition: preposition for preposition in prepositions}

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    token = models.CharField(max_length=25)
    # Prepositions *may* optionally be part of the acronym
    preposition = models.CharField(max_length=8, choices=preposition_choices, null=True)
    order = models.IntegerField()



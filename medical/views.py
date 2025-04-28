from django.http import HttpResponse
import random

def simulate_exam(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id')

        if not patient_id:
            return HttpResponse("Debes proporcionar un patient_id en la URL.", content_type="text/plain")

        exam_options = [
            'Electroencefalograma (EEG)',
            'Resonancia Magnetica Cerebral (RM)',
            'Tomografa Computarizada (TC) de craneo',
            'Prueba genetica para epilepsia',
            'Video-EEG prolongado',
            'Monitorización intracraneal',
        ]
        exam_name = random.choice(exam_options)

        exam_results = [
            'Resultado normal',
            'Actividad epiléptica detectada',
            'Lesión cerebral observada',
            'Anomalias en el lóbulo temporal',
            'Actividad eléctrica irregular',
        ]
        result = random.choice(exam_results)

        response_text = (
            f"ID del Paciente: {patient_id}\n"
            f"Examen realizado: {exam_name}\n"
            f"Resultado: {result}"
        )
        return HttpResponse(response_text, content_type="text/plain")

    else:
        return HttpResponse("Método no permitido. Usa GET.", content_type="text/plain")

def health_check(request):
    return HttpResponse("ok")
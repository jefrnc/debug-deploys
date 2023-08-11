import requests
import os

JENKINS_URL = os.environ.get('JENKINS_URL')
JENKINS_USER = os.environ.get('JENKINS_USER')
JENKINS_TOKEN = os.environ.get('JENKINS_TOKEN')
headers = {
    'Content-Type': 'application/json',
}

def get_jobs():
    response = requests.get(f'{JENKINS_URL}/api/json?tree=jobs[name,url]', auth=(JENKINS_USER, JENKINS_TOKEN), headers=headers)
    
    if response.status_code == 200:
        return response.json()['jobs']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def get_job_details(job_url):
    response = requests.get(f'{job_url}config.xml', auth=(JENKINS_USER, JENKINS_TOKEN), headers=headers)
    
    if response.status_code == 200:
        # Aquí puedes parsear el XML para extraer la información específica que necesitas.
        # Por ejemplo, el repositorio, el branch, etc.
        # Para simplificar, solo retorno el XML completo.
        return response.text
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def main():
    jobs = get_jobs()

    for job in jobs:
        print(f"Job Name: {job['name']}")
        details = get_job_details(job['url'])
        
        if details:
            # Aquí imprimes o procesas la información extraída del XML.
            # Por ahora, solo imprimo una parte del XML para no sobrecargar la salida.
            print(details[:1000] + "...")

if __name__ == "__main__":
    main()

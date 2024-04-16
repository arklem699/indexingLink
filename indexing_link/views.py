from django.shortcuts import render
import subprocess


def indexing_links(request):
    if request.method == 'POST':
        links = request.POST.get('links', '').strip()
        links = links.split('\n')
        with open('google-indexing-api-bulk-master/urls.txt', 'w', newline='\n') as f:
            for link in links:
                f.write(link + '\n')
        process = subprocess.Popen(['C:/Program Files/nodejs/node.exe', 'index.js'], stdout=subprocess.PIPE, cwd='google-indexing-api-bulk-master/')
        output, _ = process.communicate()
        return render(request, 'index.html', {'output': output.decode()})
    else:
        return render(request, 'index.html', {'output': ''})
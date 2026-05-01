import os
import zipfile

_zip = zipfile.ZipFile('./listado.zip', 'w')
for folder, subfolders, files in os.walk('./'):

    for file in files:
        if file.endswith('.py'):
            _zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'C:\\Stories\\Fantasy'),
                              compress_type=zipfile.ZIP_DEFLATED)

_zip.close()

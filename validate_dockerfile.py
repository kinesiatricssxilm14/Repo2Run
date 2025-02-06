import os
import subprocess
import threading

root_path = 'build_agent/output'
authors = [os.path.join(root_path, a) for a in os.listdir(root_path)]
full_names = []
for a in authors:
    full_names.extend([os.path.join(a, x) for x in os.listdir(a)])

def run_docker_build_normal(timeout, cwd, log_file):
    with open(f'{cwd}/Dockerfile', 'a') as a1:
        a1.write('\nRUN cd /repo && pytest --collect-only -q')
    try:
        result = subprocess.run(
            ['docker', 'build', '.', '--tag=tmp:tmp'],
            cwd=cwd,
            stdout=log_file,
            stderr=log_file,
            timeout=timeout
        )
        return result.returncode
    except subprocess.TimeoutExpired:
        with open(f'{cwd}/TIMEOUT', 'w') as w1:
            w1.write('TIMEOUT\n')
        log_file.write("TIMEOUT\n")
        return -1

def run_docker_build_poetry(timeout, cwd, log_file):
    with open(f'{cwd}/Dockerfile', 'r') as r1:
        dockerfile = r1.readlines()
    dockerfile = dockerfile[:-1]
    dockerfile.append('RUN cd /repo && poetry run pytest --collect-only -q')
    dockerfile = [x[:-1] if x.endswith('\n') else x for x in dockerfile]
    with open(f'{cwd}/Dockerfile', 'w') as w1:
        w1.write('\n'.join(dockerfile))
    try:
        result = subprocess.run(
            ['docker', 'build', '.', '--tag=tmp:tmp'],
            cwd=cwd,
            stdout=log_file,
            stderr=log_file,
            timeout=timeout
        )
        return result.returncode
    except subprocess.TimeoutExpired:
        with open(f'{cwd}/TIMEOUT', 'w') as w1:
            w1.write('TIMEOUT\n')
        log_file.write("TIMEOUT\n")
        return -1

for full_name in full_names:
    if not os.path.exists(f'{full_name}/Dockerfile'):
        print(f'{full_name}/Dockerfile not found')
        continue
    if os.path.exists(f'{full_name}/SUCCESS') or os.path.exists(f'{full_name}/FAIL') or os.path.exists(f'{full_name}/TIMEOUT'):
        continue
    print(f'Begin {full_name}')
    
    subprocess.run(['docker', 'rmi', 'tmp:tmp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    log_path = os.path.join(full_name, 'build_normal_test.log')
    with open(log_path, 'w') as log_file:
        returncode = run_docker_build_normal(600, full_name, log_file)
    
    if returncode == 0:
        success_path = os.path.join(full_name, 'SUCCESS')
        with open(success_path, 'w') as f:
            f.write('Build was successful.')
        print(f'Success: {full_name}')
    elif returncode == -1:
        timeout_path = os.path.join(full_name, 'TIMEOUT')
        with open(timeout_path, 'w') as f:
            f.write('Build timed out after 10 minutes.')
        print(f'Timeout: {full_name}')


    if not os.path.exists(f'{full_name}/SUCCESS'):
        subprocess.run(['docker', 'rmi', 'tmp:tmp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        log_path = os.path.join(full_name, 'build_poetry_test.log')
        with open(log_path, 'w') as log_file:
            returncode = run_docker_build_poetry(600, full_name, log_file)

        if returncode == 0:
            success_path = os.path.join(full_name, 'SUCCESS')
            with open(success_path, 'w') as f:
                f.write('Build was successful.')
            print(f'Success: {full_name}')
        elif returncode == -1:
            timeout_path = os.path.join(full_name, 'TIMEOUT')
            with open(timeout_path, 'w') as f:
                f.write('Build timed out after 10 minutes.')
            print(f'Timeout: {full_name}')
        else:
            fail_path = os.path.join(full_name, 'FAIL')
            with open(fail_path, 'w') as f:
                f.write('Build failed.')
            print(f'Fail: {full_name}')
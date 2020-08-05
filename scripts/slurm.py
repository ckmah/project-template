def new_slurm_script(script_name, cpus_per_task='1', mem_per_cpu='5G', array_t='1-9000', array_tc='250'):

    with open(script_name, 'w') as f:
        f.write(f'''#! /bin/bash

#SBATCH --job-name={script_name}
#SBATCH --output=/cellar/users/ckmah/logs/%A_%a.out
#SBATCH --error=/cellar/users/ckmah/logs/%A_%a.err
#SBATCH --cpus-per-task={cpus_per_task}
#SBATCH --mem-per-cpu={mem_per_cpu}
#SBATCH --array={array_t}%{array_tc}

''')


def map_slurm_task_id(script_name, file_list, var_name):

    # generate file list with ' '
    file_list_str = ' '.join(file_list)

    # 1. Save file list to bash array
    # 2. Get current file according to array task id
    with open(script_name, 'a') as f:
        f.write(f'''
{var_name}s=({file_list_str})
{var_name}=${{{var_name}s[$SLURM_ARRAY_TASK_ID -1]}}
''')

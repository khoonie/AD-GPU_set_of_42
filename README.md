# AD-GPU_set_of_42 with AutoDock-GPU

Hosted in Nvidia NGC Catalog, a Nvidia Docker container that has been setup to utilize the host machine's Nvidia GPU for processing. The CUDA Driver + Host OS running on top of Nvidia GPU and Server/PC is assumed to be already installed. The containers with AutoDock-GPU application + CUDA Toolkit runs on top of Docker Engine or Singularity.

The original check.py sample file had some errors/adjustments needed. This repo contains the modified check.py file and some instructions on how to navigate some errors encountered. Note that WSL2 + Windows 11 Pro is used. If pure Linux (Ubuntu, etc.) distros are used there may be other or less issues (not tested).

## Original Instructions
https://catalog.ngc.nvidia.com/orgs/hpc/containers/autodock
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

## Modifications
Ubuntu 22.04 on WSL2 Windows 11 Pro
Make sure the docker config in Windows Docker Desktop is also modified to include the following, similar to within WSL2 Ubuntu
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
Restart both Docker WSL2 and Windows Docker Desktop

Make sure the check.py file has +x permissions for execution by chmod +x check.py

docker run -ti --gpus all -v $HOME/Projects/AD-GPU_set_of_42 --workdir /AD-GPU_set_of_42 nvcr.io/hpc/autodock:2020.06 sh -c "./check.py"

ligand_properties.csv and check.py are in the same workdir directory "AD-GPU_set_of_42", while the script refers to "data" directory one level up, which contains all the files to be processed.

## Output

See output.txt for a sample run output

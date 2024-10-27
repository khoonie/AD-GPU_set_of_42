#!/usr/bin/env python3
import csv
import glob
import os
import re
import subprocess
import sys


def run_all(executable):
  dirlist = glob.glob("data/*")
  print ("List of dir is:")
  print (dirlist)
  for d in dirlist:
      print(d)
      os.chdir(d)
      # There's potentially 3 runs to do here, doing 1 to save time.
      for i in range(1):
          subprocess.run("{} -ffile protein.maps.fld -lfile rand-{}.pdbqt -nrun 100 -lsmet ad -heuristics 1 -autostop 1 -maxnev 8000000 -resnam CUDAout-{}".format(executable, i, i), shell=True).check_returncode()
      os.chdir("../..")


def process_file(filename):
    re_ligandname = re.compile(r'^Ligand name: (.+)')
    re_intermolecular = re.compile(r'^(?=.*\bIntermolecular\b).*=(.*)')
    re_internal = re.compile(r'^(?=.*\bInternal\b).*=(.*)')
    ligand = ''
    curr_energy = sys.float_info.max
    best_energy = sys.float_info.max
    with open(filename) as f:
        for line in f:
            match = re_ligandname.search(line)
            if match:
                ligand = match.group(0).split()[2]
                continue
            match = re_intermolecular.search(line)def check_output(reference_energies):
    results = {}
    err = 0.0
    cnt = 0
    for key, val in reference_energies.items():
        for dlgfile in glob.glob('data/*/CUDAout-*.dlg'):
           best_energy = process_file(dlgfile)
           diff = val - best_energy
           err = err + diff
           cnt = cnt + 1
           try:
               results[key].append(diff)
           except KeyError:
               results[key] = [diff]
    return (err/cnt)

reference_energies = {}
with open('ligand_properties.csv') as f:
    reader = csv.reader(f)
    cnt = 0
    for row in reader:
        print(row)
        cnt = cnt + 1
        if cnt == 1:
            continue
        # There are some bad ligands for which we have no reference energy
        if row[4] == '':
            continue
        reference_energies[row[1]] = float(row[4])

for numwi in [128]:
    run_all("autodock_gpu_{}wi".format(numwi))
    meandiff = check_output(reference_energies)
    print('{} : Mean Error: {:.3f}'.format(numwi, meandiff))
    if meandiff >  0.5:
        exit(1)

print("Checks passed.")
            if match:
                curr_energy = float(match.group(1).split()[0])
                continue
            match = re_internal.search(line)
            if match:
                curr_energy = curr_energy + float(match.group(1).split()[0])
                if (curr_energy <  best_energy):
                    best_energy = curr_energy
                continue
    return best_energy


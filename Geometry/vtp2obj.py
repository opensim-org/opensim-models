#!/usr/bin/env python3

import argparse
import os
import vtk

def print_as_obj(vtp_path):
    filename, ext = os.path.splitext(vtp_path)

    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(vtp_path)
    writer = vtk.vtkOBJWriter()
    writer.SetInputConnection(reader.GetOutputPort())
    writer.SetFileName(f'{filename}.obj')
    writer.Write()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    args = parser.parse_args()
    print_as_obj(args.input_file)

if __name__ == '__main__':
    main()


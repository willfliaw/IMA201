# Introduction to Image Processing (IMA201) - 2023/2024

## Course Overview

This repository contains materials and resources for the course **Introduction to Image Processing (IMA201)**, part of the **Image-Data-Signal** curriculum. The course introduces the fundamentals of digital image processing, covering image acquisition, restoration, and analysis techniques.

### Key Topics:

- Image Acquisition: Optics, sampling, noise, radiometry, and color.
- Image Restoration: Denoising, inverse problems, deconvolution, super-resolution, and inpainting.
- Image Analysis: Differential operators, segmentation, local descriptors, texture, and shape representation.
- Mathematical Tools: Multi-scale Gaussian and Laplacian representations, wavelet decompositions, discrete representations, and mathematical morphology.

## Prerequisites

Students are expected to have basic knowledge of:
- Mathematics (linear algebra, calculus)
- General programming skills

## Course Structure

- Total Hours: 24 hours
- Credits: 2.5 ECTS
- Evaluation: 50% written exam, 50% project (with practical work reports serving as bonuses/maluses).

## Instructor

- Professor Yann Gousseau

## Installation and Setup

Some exercises and projects require Python and relevant image processing libraries. You can follow the instructions below to set up your environment using `conda`:

1. Anaconda/Miniconda: Download and install Python with Anaconda or Miniconda from [Conda Official Site](https://docs.conda.io/en/latest/).
2. Image Processing Libraries: Create a new conda environment with the necessary packages:
   ```bash
   conda create -n ima python matplotlib numpy scipy scikit-image ipykernel pandas scikit-learn jupyter tqdm bokeh opencv munkres
   ```
3. Activate the environment:
   ```bash
   conda activate ima
   ```

4. Launch Jupyter Notebook (if required for exercises):
   ```bash
   jupyter notebook
   ```

This will set up the necessary environment for running image processing tasks and exercises for the course.

## How to Contribute

Feel free to contribute to the repository by:
- Submitting pull requests for corrections or improvements.
- Providing additional examples or extending the projects.

# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname diffusers

Name:           python-%{srcname}
Version:        0.37.1
Release:        %autorelease
Summary:        State-of-the-art diffusion models for image, video, and audio generation in PyTorch
License:        Apache-2.0
URL:            https://github.com/huggingface/diffusers
#!RemoteAsset:  sha256:2346c21f77f835f273b7aacbaada1c34a596a3a2cc6dc99d149efcd0ec298fa
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Core install_requires only; modules below need optional dependencies not present:
#   No module named 'flax' / 'jax' — all *_flax modules - extra[flax]
#   No module named 'transformers' — all pipelines / modular_pipelines - extra[test]
#   No module named 'tokenizers' — loaders.textual_inversion - extra[test]
#   No module named 'gguf' — quantizers.gguf.utils  - extras[gguf]
#   No module named 'torchsde' — schedulers.scheduling_dpmsolver_sde (and cosine variant) - extra[test]
BuildOption(check):  -e '*flax*'
BuildOption(check):  -e 'diffusers.*pipelines*'
BuildOption(check):  -e 'diffusers.loaders.textual_inversion'
BuildOption(check):  -e 'diffusers.quantizers.gguf.utils'
BuildOption(check):  -e 'diffusers.schedulers.scheduling_dpmsolver_sde'
BuildOption(check):  -e 'diffusers.schedulers.scheduling_cosine_dpmsolver_multistep'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Diffusers is the go-to library for state-of-the-art pretrained diffusion
models for generating images, audio, and even 3D structures of molecules.
Whether you're looking for a simple inference solution or training your own
diffusion models, Diffusers is a modular toolbox that supports both. The
library is designed with a focus on usability over performance, simple over
easy, and customizability over abstractions.

Diffusers offers three core components:
- State-of-the-art diffusion pipelines that can be run in inference with
  just a few lines of code.
- Interchangeable noise schedulers for different diffusion speeds and
  output quality.
- Pretrained models that can be used as building blocks, and combined with
  schedulers, for creating your own end-to-end diffusion systems.

# training and test suit are not satisfied on openRuyi
%pyproject_extras_subpkg -n python-%{srcname} torch training test

%generate_buildrequires
%pyproject_buildrequires -x torch

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/diffusers-cli

%changelog
%autochangelog

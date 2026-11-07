# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname diffusers

Name:           python-%{srcname}
Version:        0.42.1
Release:        %autorelease
Summary:        State-of-the-art diffusion models for image, video, and audio generation in PyTorch
License:        Apache-2.0
URL:            https://github.com/huggingface/diffusers
#!RemoteAsset:  sha256:ce855ab670c8cd1c7a61be8f12fbc68c081bca8ec5e747273946d8d6c2aff23b
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Patch2000:      2000-Allow-current-test-and-training-dependency-versions.patch
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(prep):  -p1
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
# The optional Nunchaku loader imports Hugging Face kernels at module import time.
BuildOption(check):  -e 'diffusers.quantizers.nunchaku.utils'
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

%pyproject_extras_subpkg -n python-%{srcname} torch training test

%generate_buildrequires
%pyproject_buildrequires -x torch

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/diffusers-cli

%changelog
%autochangelog

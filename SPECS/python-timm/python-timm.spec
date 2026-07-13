# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname timm

Name:           python-%{srcname}
Version:        1.0.28
Release:        %autorelease
Summary:        PyTorch image models, layers, and utilities
License:        Apache-2.0
URL:            https://github.com/huggingface/pytorch-image-models
VCS:            git:https://github.com/huggingface/pytorch-image-models.git
#!RemoteAsset:  sha256:3789d313fdd5541a327b60180d70dbb4bdec73db8ff0655e413db3c3d134a9a4
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
# Skip optional TensorFlow dataset reader: No module named 'tensorflow'.
BuildOption(check):  -e timm.data.readers.reader_tfds
# Skip optional TensorFlow preprocessing helpers: No module named 'tensorflow'.
BuildOption(check):  -e timm.data.tf_preprocessing

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(huggingface-hub)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(safetensors)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(torchvision)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyTorch Image Models provides image model architectures, layers, utilities,
optimizers, schedulers, data loaders, and augmentations for PyTorch.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

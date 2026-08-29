# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname compressed-tensors
%global pypi_name compressed_tensors

Name:           python-%{srcname}
Version:        0.15.0.1
Release:        %autorelease
Summary:        Library for utilization of compressed safetensors of neural network models
License:        Apache-2.0
URL:            https://github.com/vllm-project/compressed-tensors
#!RemoteAsset:  sha256:a8e93054e8a5ec49c980b09ed36c4c1249b4a8ee167920a8e461c4da26e78d99
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(psutil)

Requires:       python3dist(psutil)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A safetensors extension to efficiently store sparse quantized tensors on disk.

%prep -a
sed -i 's/setuptools_scm==8.2.0/setuptools_scm>=8.2.0/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname kernels

Name:           python-%{srcname}
Version:        0.16.0
Release:        %autorelease
Summary:        Download and load compute kernels
License:        Apache-2.0
URL:            https://github.com/huggingface/kernels
VCS:            git:https://github.com/huggingface/kernels.git
#!RemoteAsset:  sha256:5a4118396b9866209e767973d697d3f2ee76f6ed1b2f72269b72f8cd4dc90a7f
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
BuildOption(check):  %{srcname}

BuildRequires:  libomp-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(huggingface-hub) >= 1.10
BuildRequires:  python3dist(kernels-data) >= 0.14.0~dev1
BuildRequires:  python3dist(packaging) >= 20
BuildRequires:  python3dist(pyyaml) >= 6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sigstore) >= 4
BuildRequires:  python3dist(sigstore) < 5
BuildRequires:  python3dist(tomlkit) >= 0.13.3
BuildRequires:  python3dist(torch)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       libomp
Requires:       python3dist(torch)

%description
Kernels downloads, verifies, and loads prebuilt compute kernels from the
Hugging Face Hub.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/kernels

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname einops

Name:           python-%{srcname}
Version:        0.8.2
Release:        %autorelease
Summary:        A new flavour of deep learning operations
License:        MIT
URL:            https://github.com/arogozhnikov/einops
VCS:            git:https://github.com/arogozhnikov/einops
#!RemoteAsset:  sha256:609da665570e5e265e27283aab09e7f279ade90c4f01bcfca111f3d3e13f2827
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Flexible and powerful tensor operations for readable and reliable code.
Einops provides a concise notation for tensor rearrangement, reduction,
repetition, packing, unpacking, and einsum across multiple array frameworks.

%generate_buildrequires
%pyproject_buildrequires

# No check for this package
%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

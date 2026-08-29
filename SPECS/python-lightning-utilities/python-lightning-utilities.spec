# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lightning-utilities
%global pypi_name lightning_utilities

Name:           python-%{srcname}
Version:        0.15.3
Release:        %autorelease
Summary:        PyTorch Lightning utilities
License:        Apache-2.0
URL:            https://github.com/Lightning-AI/utilities
#!RemoteAsset:  sha256:792ae0204c79f6859721ac7f386c237a33b0ed06ba775009cb894e010a842033
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Common utilities for the PyTorch Lightning ecosystem.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

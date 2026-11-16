# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global srcname modelscope-hub
%global pypi_name modelscope_hub

Name:           python-modelscope-hub
Version:        0.4.6
Release:        %autorelease
Summary:        Python client for the ModelScope Hub
License:        Apache-2.0
URL:            https://pypi.org/project/modelscope-hub/
VCS:            git:https://github.com/modelscope/modelscope_hub
#!RemoteAsset:  sha256:c54de09be2ccb27b9214f7c3ebe5751121f335f5016643f789589d0547e78c52
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l modelscope_hub
BuildOption(install):  +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-modelscope-hub = %{version}-%{release}
%python_provide python3-modelscope-hub

Requires:       python3dist(cryptography) >= 41
Requires:       python3dist(filelock) >= 3.9
Requires:       python3dist(requests) >= 2.28
Requires:       python3dist(tqdm) >= 4.64.0
Requires:       python3dist(urllib3) >= 1.26

%description
The official Python client for connecting to and working with the ModelScope
Hub, including model and dataset downloads and the compatible legacy hub API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

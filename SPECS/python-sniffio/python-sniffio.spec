# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sniffio

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Sniff out which async library your code is running under
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/sniffio
#!RemoteAsset:  sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a package for detecting which async library code is running
under. It supports multiple async I/O packages, like Trio, and
asyncio.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

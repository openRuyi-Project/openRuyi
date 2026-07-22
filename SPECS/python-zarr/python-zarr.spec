# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zarr

Name:           python-%{srcname}
Version:        3.2.1
Release:        %autorelease
Summary:        Chunked compressed N-dimensional arrays
License:        MIT
URL:            https://github.com/zarr-developers/zarr-python
#!RemoteAsset:  sha256:71565b738a0e7e8ed226f0516eba8c6bb53440ad7669a8c48ebb3534a161d035
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l zarr

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(donfig)
BuildRequires:  python3dist(google-crc32c)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(numcodecs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Zarr is an implementation of chunked, compressed, N-dimensional arrays
for Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/zarr

%changelog
%autochangelog

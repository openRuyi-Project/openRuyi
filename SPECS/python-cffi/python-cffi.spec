# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cffi

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Foreign function interface for Python
License:        MIT
URL:            https://cffi.readthedocs.io/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  libffi-devel
BuildRequires:  pkg-config
BuildRequires:  gcc
BuildSystem:    pyproject
BuildOption(install):   _cffi_backend cffi
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
%description
Foreign Function Interface for Python calling C code.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README*

%changelog
%autochangelog

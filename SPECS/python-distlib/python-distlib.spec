# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname distlib

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        Distribution utilities
License:        Python-2.0
URL:            https://github.com/pypa/distlib
#!RemoteAsset:  sha256:feec40075be03a04501a973d81f633735b4b69f98b05450592310c0f401a4e0d
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Distlib is a library which implements low-level functions that
relate to packaging and distribution of Python software.  It is intended to be
used as the basis for third-party packaging tools.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
rm distlib/*.exe

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog

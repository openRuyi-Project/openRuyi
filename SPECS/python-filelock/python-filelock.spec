# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname filelock

Name:           python-%{srcname}
Version:        3.20.0
Release:        %autorelease
Summary:        Platform independent file lock
License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
#!RemoteAsset:  sha256:711e943b4ec6be42e1d4e6690b48dc175c822967466bb31c0c293f34334c13f4
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
filelock contains a single module implementing
a platform independent file lock in Python, which provides a simple way of
inter-process communication.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog

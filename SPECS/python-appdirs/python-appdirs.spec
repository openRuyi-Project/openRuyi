# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname appdirs

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
Summary:        Determine platform-specific dirs, e.g. a "user data dir"
License:        MIT
URL:            https://github.com/ActiveState/appdirs
#!RemoteAsset:  sha256:7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog

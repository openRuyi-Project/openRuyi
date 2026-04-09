# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname appdirs

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
License:        MIT
URL:            https://github.com/ActiveState/appdirs
Summary:        Determine platform-specific dirs, e.g. a "user data dir"
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".


%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc  README.rst CHANGES.rst

%changelog
%autochangelog

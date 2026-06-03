# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests-toolbelt
%global import_name requests_toolbelt

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Utility belt for advanced users of python-requests
License:        Apache-2.0
URL:            https://toolbelt.readthedocs.io/
VCS:            git:https://github.com/requests/toolbelt.git
#!RemoteAsset:  sha256:7681a0a3d047012b5bdc0ee37d7f8f07ebe76ab08caeccfc3921ce23c88d5bc6
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{import_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       python3dist(pyopenssl)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Requests Toolbelt is a collection of utilities for advanced users of the
python-requests HTTP library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst HISTORY.rst AUTHORS.rst
%license LICENSE

%changelog
%autochangelog

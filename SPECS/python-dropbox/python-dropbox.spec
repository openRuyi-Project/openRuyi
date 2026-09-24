# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dropbox

Name:           python-%{srcname}
Version:        12.2.1
Release:        %autorelease
Summary:        Official Dropbox API client for Python
License:        MIT
URL:            https://www.dropbox.com/developers
VCS:            git:https://github.com/dropbox/dropbox-sdk-python.git
#!RemoteAsset:  sha256:61fcb821f7e8585aa4b9e2abc94801aaf8d65ed5ca89313450e56d51c46add7e
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch2000:      2000-allow-setuptools-scm-10.patch

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(requests) >= 2.16.2
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(stone) >= 3.5.3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides the official Python client library for the Dropbox API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog

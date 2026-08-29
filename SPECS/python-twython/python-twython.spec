# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname twython

Name:           python-%{srcname}
Version:        3.9.1
Release:        %autorelease
Summary:        Actively maintained, pure Python wrapper for the Twitter API
License:        MIT
URL:            https://github.com/ryanmcgrath/twython
#!RemoteAsset:  sha256:5a3f0ac24d10705257028fb4205bfedf432ff28d358b796e0c2f01a2f9990c84
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Twython is an actively maintained, pure Python wrapper for the Twitter
API. It supports both normal and streaming Twitter APIs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rfc3987

Name:           python-%{srcname}
Version:        1.3.8
Release:        %autorelease
Summary:        Parsing and validation of URIs and IRIs
License:        GPL-3.0-or-later
URL:            https://github.com/dgerber/rfc3987
#!RemoteAsset:  sha256:d3c4d257a560d544e9826b38bc81db676890c79ab9d7ac92b39c7a253d5ca733
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l rfc3987

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rfc3987 provides parsing and validation helpers for RFC 3986 URIs and RFC
3987 IRIs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.txt

%changelog
%autochangelog

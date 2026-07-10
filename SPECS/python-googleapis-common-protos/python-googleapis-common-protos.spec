# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname googleapis-common-protos
%global pypi_name googleapis_common_protos

Name:           python-%{srcname}
Version:        1.75.0
Release:        %autorelease
Summary:        Common protobufs used in Google APIs
License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
VCS:            git:https://github.com/googleapis/python-api-common-protos.git
#!RemoteAsset:  sha256:53a062ff3c32552fbd62c11fe23768b78e4ddf0494d5e5fd97d3f4689c75fbbd
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l google -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package contains common protocol buffer types used by Google APIs. These
definitions provide Python modules under the google namespace for shared API
annotations and types.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog

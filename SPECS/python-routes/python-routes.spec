# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname routes
%global pypi_name Routes

Name:           python-%{srcname}
Version:        2.5.1
Release:        %autorelease
Summary:        Routing recognition and generation tools
License:        MIT
URL:            https://routes.readthedocs.io/
VCS:            git:https://github.com/bbangert/routes.git
#!RemoteAsset:  sha256:b6346459a15f0cbab01a45a90c3d25caf980d4733d628b4cc1952b865125d053
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
# routes.middleware imports webob (the middleware extra), needed by the
# default import check
BuildRequires:  python3dist(webob)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Routes is a Python re-implementation of the Rails routes system for mapping
URLs to controllers/actions and generating URLs. Routes makes it easy to
create pretty and concise URLs that are RESTful with little effort.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog

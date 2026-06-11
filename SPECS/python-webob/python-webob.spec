# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname webob

Name:           python-%{srcname}
Version:        1.8.10
Release:        %autorelease
Summary:        WSGI request and response objects
License:        MIT
URL:            https://webob.org/
VCS:            git:https://github.com/Pylons/webob.git
#!RemoteAsset:  sha256:1c963a11f307bc3f624fbab9dde737701eae255f32981b7a5486a88db1767c2b
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
WebOb provides objects for HTTP requests and responses. Specifically it
does this by wrapping the WSGI request environment and response
status/headers/app_iter (body). The request and response objects provide
many conveniences for parsing HTTP request and forming HTTP responses.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

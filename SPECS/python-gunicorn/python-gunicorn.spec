# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gunicorn

Name:           python-%{srcname}
Version:        26.0.0
Release:        %autorelease
Summary:        WSGI HTTP server for UNIX
License:        MIT
URL:            https://gunicorn.org
VCS:            git:https://github.com/benoitc/gunicorn.git
#!RemoteAsset:  sha256:ca9346f85e3a4aeeb64d491045c16b9a35647abd37ea15efe53080eb8b090baf
Source:         https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.app.pasterapp" -e "%{srcname}.workers.geventlet" -e "%{srcname}.workers.ggevent"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tornado)

Requires:       python3dist(packaging)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Gunicorn is a Python WSGI HTTP server for UNIX. It is a pre-fork worker model
server ported from Ruby Unicorn. It supports various worker types and is
commonly used to serve Flask and Django applications in production.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE NOTICE
%doc README.md
%{_bindir}/gunicorn
%{_bindir}/gunicornc

%changelog
%autochangelog

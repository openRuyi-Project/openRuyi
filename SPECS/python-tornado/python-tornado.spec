# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tornado

Name:           python-%{srcname}
Version:        6.5.10
Release:        %autorelease
Summary:        Scalable, non-blocking web server and tools
License:        Apache-2.0
URL:            https://github.com/tornadoweb/tornado
#!RemoteAsset:  sha256:a6b1ccd08c04b4a06fb5aeb381be99de5ad1e5375c1785e31d78c880feb57687
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# skip the test as we don't have twisted yet.
Patch0:         0001-skip-twisted-test.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pycares)
BuildRequires:  python3dist(pycurl)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# The optional CaresResolver uses gethostbyname, removed in pycares 5.
%pytest --pyargs tornado.test -k 'not CaresResolverTest'

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

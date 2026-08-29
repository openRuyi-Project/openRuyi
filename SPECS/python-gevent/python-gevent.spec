# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gevent

Name:           python-%{srcname}
Version:        26.4.0
Release:        %autorelease
Summary:        Coroutine-based network library
License:        MIT
URL:            https://github.com/gevent/gevent
VCS:            git:https://github.com/gevent/gevent.git
#!RemoteAsset:  sha256:288d03addfccf0d1c67268358b6759b04392bf3bc35d26f3d9a45c82899c292d
Source:         https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.tests*" -e "%{srcname}.testing*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(dnspython)

Requires:       python3dist(greenlet)
Requires:       python3dist(zope-event)
Requires:       python3dist(zope-interface)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
gevent is a coroutine-based Python networking library that uses greenlet to
provide a high-level synchronous API on top of the libev or libuv event loop.
Features include lightweight execution units based on greenlets, a familiar API
that re-uses concepts from the Python standard library, cooperative sockets
with SSL support, DNS queries performed through a threadpool or c-ares, and the
ability to use standard library interfaces with cooperative sockets.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE NOTICE
%doc README.rst CHANGES.rst AUTHORS

%changelog
%autochangelog

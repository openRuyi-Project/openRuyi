# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyzmq

Name:           python-%{srcname}
Version:        27.1.0
Release:        %autorelease
Summary:        Python bindings for zeromq
License:        BSD-3-Clause AND LGPL-2.1-or-later AND Apache-2.0
URL:            https://github.com/zeromq/pyzmq
#!RemoteAsset:  sha256:ac0765e3d44455adb6ddbf4417dcce460fc40a05978c08efdf2948072f6db540
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -Ccmake.define.PYZMQ_LIBZMQ_RPATH:BOOL=OFF
BuildOption(build):  -Ccmake.define.PYZMQ_NO_BUNDLE=ON
BuildOption(build):  -Clogging.level=INFO
BuildOption(build):  -Cbuild.verbose=true
BuildOption(build):  -Ccmake.build-type="RelWithDebInfo"
BuildOption(install):  -L zmq
# The cffi backend does not apply when we build with Cython.
BuildOption(check):  -e 'zmq.backend.cffi*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pysocks)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(gevent)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package contains Python bindings for ZeroMQ. ØMQ is a lightweight and fast
messaging implementation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md licenses/

%changelog
%autochangelog

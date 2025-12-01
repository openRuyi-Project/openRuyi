# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tevent
Version:        0.17.1
Release:        %autorelease
Summary:        The tevent library
License:        LGPL-3.0-or-later
URL:            https://tevent.samba.org/
# TODO: We can't get a VCS link for tevent...
VCS:            git:https://git.samba.org/samba.git
#!RemoteAsset
Source0:        https://download.samba.org/pub/tevent/tevent-%{version}.tar.gz
#!RemoteAsset
Source1:        https://download.samba.org/pub/tevent/tevent-%{version}.tar.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --bundled-libraries=NONE
BuildOption(conf):  --builtin-libraries=replace

BuildRequires:  make
BuildRequires:  libxslt
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  python3-devel
BuildRequires:  python3-talloc-devel

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package        devel
Summary:        Developer tools for the Tevent library
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(talloc)

%description devel
Header files needed to develop programs that link against the Tevent library.

%package     -n python-tevent
Summary:        Python bindings for the Tevent library
Provides:       python3-tevent
Requires:       %{name} = %{version}-%{release}
%python_provide python3-tevent

%description -n python-tevent
Python bindings for tevent

%conf -p
# workaround https://gitlab.com/ita1024/waf/-/issues/2472
export PYTHONARCHDIR=%{python3_sitearch}

%files
%license LICENSE
%{_libdir}/libtevent.so.*

%files devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc

%files -n python-tevent
%{python3_sitearch}/tevent.py
# TODO: figure out why we don't have this - 251
#{python3_sitearch}/__pycache__/tevent.*
%{python3_sitearch}/_tevent.cpython*.so

%changelog
%{?autochangelog}

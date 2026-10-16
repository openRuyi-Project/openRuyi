# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0


Name:           tevent
Version:        0.17.2
Release:        %autorelease
Summary:        The tevent library
License:        LGPL-3.0-or-later
URL:            https://tevent.samba.org/
VCS:            git:https://git.samba.org/samba.git
#!RemoteAsset:  sha256:e53b1ac288d017d66dde0471cd429a806168ecf07179d7f019572d7a7e05f0d6
Source0:        https://download.samba.org/pub/tevent/tevent-%{version}.tar.gz
BuildSystem:    waf

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --bundled-libraries=NONE
BuildOption(conf):  --builtin-libraries=replace

BuildRequires:  libxslt
BuildRequires:  pkgconfig(cmocka) >= 1.1.8
BuildRequires:  pkgconfig(talloc) >= 2.5.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-talloc-devel >= 2.5.0

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package        devel
Summary:        Developer tools for the Tevent library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(talloc)

%description devel
Header files needed to develop programs that link against the Tevent library.

%package     -n python-tevent
Summary:        Python bindings for the Tevent library
Provides:       python3-tevent = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-tevent
Python bindings for tevent


%files
%license LICENSE
%{_libdir}/libtevent.so.*

%files devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc

%files -n python-tevent
%{python3_sitearch}/tevent.py
%{python3_sitearch}/_tevent.cpython*.so

%changelog
%autochangelog

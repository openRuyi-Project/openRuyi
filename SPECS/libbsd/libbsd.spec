# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global optflags %{optflags} -ffat-lto-objects

Name:           libbsd
Version:        0.12.2
Release:        %autorelease
Summary:        Library with functions commonly found on BSD systems
License:        BSD-3-Clause
URL:            https://libbsd.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/libbsd/libbsd.git
#!RemoteAsset:  sha256:b88cc9163d0c652aaf39a99991d974ddba1c3a9711db8f1b5838af2a14731014
Source0:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  pkgconfig(libmd)

BuildOption(conf):  --disable-static

%description
This library provides functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package        devel
Summary:        Development headers and files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libmd)

%description    devel
This library provides functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port projects
with strong BSD origins, without needing to embed the same code over and
over again on each project.

%package        ctor-static
Summary:        Development headers and files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".

%files
%license COPYING
%doc ChangeLog
%{_libdir}/libbsd.so.0*

%files devel
%{_includedir}/bsd
%{_libdir}/libbsd.so
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_libdir}/pkgconfig/libbsd.pc
%{_libdir}/pkgconfig/libbsd-overlay.pc

%files ctor-static
%{_libdir}/libbsd-ctor.a
%{_libdir}/pkgconfig/libbsd-ctor.pc

%changelog
%autochangelog

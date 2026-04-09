# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gc
Version:        8.2.8
Release:        %autorelease
Summary:        A garbage collector for C and C++
# This is a special MIT-style-License
License:        LicenseRef-GC-MIT
URL:            http://www.hboehm.info/gc/
VCS:            git:https://github.com/bdwgc/bdwgc/
#!RemoteAsset
Source0:        https://github.com/bdwgc/bdwgc/releases/download/v%{version}/gc-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-docs
BuildOption(conf):  --enable-cplusplus
BuildOption(conf):  --enable-large-config
BuildOption(conf):  --enable-threads=posix

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libtool

%description
The Boehm-Demers-Weiser conservative garbage collector can be
used as a garbage collecting replacement for C malloc or C++ new.

%package        devel
Summary:        Libraries and header files for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%install -a
install -p -D -m644 doc/gc.man  %{buildroot}%{_mandir}/man3/gc.3
## Delete unpackaged files
rm -rfv %{buildroot}%{_datadir}/gc/

%files
%doc AUTHORS ChangeLog README.md
%{_libdir}/libcord.so.1*
%{_libdir}/libgc.so.1*
%{_libdir}/libgccpp.so.1*
%{_libdir}/libgctba.so*

%files devel
%doc doc/README.environment doc/README.linux
%{_includedir}/gc.h
%{_includedir}/gc_cpp.h
%{_includedir}/gc/
%{_libdir}/libcord.so
%{_libdir}/libgc.so
%{_libdir}/libgccpp.so
%{_libdir}/pkgconfig/bdw-gc.pc
%{_mandir}/man3/gc.3*

%changelog
%autochangelog

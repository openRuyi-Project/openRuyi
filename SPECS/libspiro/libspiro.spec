# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libspiro
Version:        20240903
Release:        %autorelease
Summary:        Library implementing the Unicode Bidirectional Algorithm
License:        GPL-3.0-or-later
URL:            https://github.com/fontforge/libspiro
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-dist-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make

%description
This library will take an array of spiro control points and
convert them into a series of bézier splines which can then
be used in the myriad of ways the world has come to use béziers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc README* ChangeLog AUTHORS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspiro.pc
%{_mandir}/man3/libspiro.3.gz

%changelog
%autochangelog

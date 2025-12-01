# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libestr
Version:        0.1.11
Release:        %autorelease
Summary:        String handling essentials library
License:        LGPL-2.1-or-later
URL:            http://libestr.adiscon.com/
#!RemoteAsset
Source0:        http://libestr.adiscon.com/files/download/libestr-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --with-pic

BuildRequires:  gcc

%description
libestr is a library for some string essentials, used by projects like rsyslog.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%install -a
rm -f %{buildroot}%{_libdir}/*.{a,la}

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libestr.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libestr.pc

%changelog
%{?autochangelog}

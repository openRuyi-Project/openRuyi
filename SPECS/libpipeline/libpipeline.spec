# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpipeline
Version:        1.5.8
Release:        %autorelease
Summary:        A C library for manipulating pipelines of subprocesses
License:        GPL-3.0-or-later
URL:            https://libpipeline.nongnu.org/
VCS:            git:https://gitlab.com/libpipeline/libpipeline.git
#!RemoteAsset
Source:         https://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(check)

%description
libpipeline is a C library for manipulating pipelines of subprocesses
in a flexible and convenient way. This allows you to create pipelines
such as fork and execve easily and safely.

%package        devel
Summary:        Development files and documentation for libpipeline
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, pkg-config file, and
API documentation needed for development with libpipeline.

%files
%license COPYING
%doc ChangeLog
%{_libdir}/libpipeline.so*

%files devel
%{_libdir}/libpipeline.so
%{_libdir}/pkgconfig/libpipeline.pc
%{_includedir}/*.h
%{_mandir}/man3/*

%changelog
%{?autochangelog}

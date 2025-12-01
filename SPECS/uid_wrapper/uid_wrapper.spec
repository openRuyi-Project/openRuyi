# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           uid_wrapper
Version:        1.3.2
Release:        %autorelease
Summary:        A wrapper for privilege separation
License:        GPL-3.0-or-later
URL:            http://cwrap.org/
#!RemoteAsset
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
BuildSystem:    cmake

BuildOption(conf):  -DUNIT_TESTING=ON

BuildRequires:  cmake
BuildRequires:  cmocka-cmake

Recommends:     cmake
Recommends:     pkgconfig

%description
Some projects like a file server need privilege separation to be able to switch
to the connection user and do file operations. uid_wrapper convincingly lies
to the application letting it believe it is operating as root and even
switching between UIDs and GIDs as needed.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
UID_WRAPPER=1

This package doesn't have a devel package cause this project is for
development/testing.

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libuid_wrapper.so*
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/uid_wrapper
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config-version.cmake
%{_libdir}/cmake/uid_wrapper/uid_wrapper-config.cmake
%{_libdir}/pkgconfig/uid_wrapper.pc
%{_mandir}/man1/uid_wrapper.1*

%changelog
%{?autochangelog}

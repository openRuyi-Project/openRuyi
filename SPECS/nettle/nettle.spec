# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nettle
Version:        3.10.2
Release:        %autorelease
Summary:        GNU file archiving program
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://www.lysator.liu.se/~nisse/nettle/
VCS:            git:https://git.lysator.liu.se/nettle/nettle.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(gmp)
BuildRequires:  m4
BuildRequires:  pkgconfig

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%package        devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gmp)

%description    devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing
applications with nettle.

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/nettle-lfib-stream
%{_bindir}/nettle-pbkdf2
%{_bindir}/pkcs1-conv
%{_bindir}/sexp-conv
%{_bindir}/nettle-hash
%{_libdir}/libnettle.so*
%{_libdir}/libhogweed.so*

%files devel
%doc descore.README nettle.html nettle.pdf
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nspr
Version:        4.37.0
Release:        %autorelease
Summary:        Netscape Portable Runtime libraries
License:        MPL-2.0
URL:            https://firefox-source-docs.mozilla.org/nspr/index.html
#!RemoteAsset
Source0:        https://ftp.mozilla.org/pub/nspr/releases/v4.37/src/%{name}-4.37.tar.gz#/%{name}-%{version}.tar.gz
Patch:                    0001-nspr-gcc-atomics.patch
BuildSystem:    autotools

BuildOption(conf): --enable-64bit --enable-optimize --disable-debug
BuildOption(conf): --includedir=%{_includedir}/nspr

BuildOption(build): -C nspr
BuildOption(install): -C nspr

BuildRequires:  gcc

%description
NetScape Portable Runtime (NSPR) provides platform independence for non-GUI
operating system facilities, including threads, I/O, and memory management.

%package devel
Summary:        Development libraries and tools for NSPR
Requires:       %{name} = %{version}

%description devel
This package contains the header files, pkg-config file, and development
tools needed to build applications that use the NSPR libraries.

%conf -p
cd nspr

%install -a
rm -f %{buildroot}%{_bindir}/compile-et.pl %{buildroot}%{_bindir}/prerr.properties
find %{buildroot} -type f -name "*.a" -delete -print

%files
%license nspr/LICENSE
%{_libdir}/lib*.so

%files devel
%{_includedir}/nspr/nspr.h
%{_includedir}/nspr/pr*.h
%{_includedir}/nspr/pl*.h
%{_includedir}/nspr/obsolete/
%{_includedir}/nspr/private/
%{_includedir}/nspr/md/
%{_bindir}/nspr-config
%{_datadir}/aclocal/nspr.m4
%{_libdir}/pkgconfig/nspr.pc

%changelog
%{?autochangelog}

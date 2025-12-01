# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           keyutils
Version:        1.6.3
Release:        %autorelease
Summary:        Linux Key Management Utilities and Libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/
#!RemoteAsset
Source:         https://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git/snapshot/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build): NO_ARLIB=1 CFLAGS="%{optflags}"
BuildOption(install): NO_ARLIB=1 DESTDIR=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_sbindir} LIBDIR=%{_libdir} USRLIBDIR=%{_libdir}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Utilities to control the kernel key management facility.
This package contains the command-line tools and runtime libraries.

%package     devel
Requires:       %{name} = %{version}-%{release}
Summary:        Development package for building linux key management utilities

%description  devel
This package provides headers and libraries for building key utilities.

# No configure
%conf

%install -a
install -m 0750 -d \
        %{buildroot}%{_sysconfdir}/keys \
        %{buildroot}%{_sysconfdir}/keys/ima \
        %{buildroot}%{_sysconfdir}/keys/evm

pushd %{buildroot}%{_libdir}
ln -sf libkeyutils.so.1 libkeyutils.so
popd

%files
%license LICENCE.GPL LICENCE.LGPL
%doc README

%{_sbindir}/*
%{_bindir}/*
%{_datadir}/keyutils
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/request-key.conf
%dir %{_sysconfdir}/request-key.d/
%dir %{_sysconfdir}/keys/
%dir %{_sysconfdir}/keys/ima/
%dir %{_sysconfdir}/keys/evm/
%{_libdir}/libkeyutils.so.*

%files devel
%{_libdir}/libkeyutils.so
%{_includedir}/*
%attr(0644, root, root) %{_libdir}/pkgconfig/libkeyutils.pc

%changelog
%{?autochangelog}

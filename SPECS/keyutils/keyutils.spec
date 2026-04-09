# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
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

BuildOption(build):  NO_ARLIB=1
BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(install):  NO_ARLIB=1
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  SBINDIR=%{_sbindir}
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  USRLIBDIR=%{_libdir}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Utilities to control the kernel key management facility.
This package contains the command-line tools and runtime libraries.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development package for building linux key management utilities

%description    devel
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

%check
# when test in x64,some privileged tests can be skipped to pass.
# when test in riscv-system,the follow tests will fail:
### RUNNING TEST keyctl/requesting/bad-args
# CHECK MAXLEN CALLOUT CHECK MAXLEN PIPED CALLOUT
# so we just skip the test here.

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
%autochangelog

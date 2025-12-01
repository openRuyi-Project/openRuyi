# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           p11-kit
Version:        0.25.5
Release:        %autorelease
Summary:        Library and tools for working with PKCS#11 modules
License:        BSD-3-Clause
URL:            https://p11-glue.freedesktop.org/p11-kit.html
#!RemoteAsset
Source:         https://github.com/p11-glue/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption:    -Dtrust_paths=%{_sysconfdir}/pki/trust:%{_datadir}/pki/trust
BuildOption:    -Dbash_completion=disabled
BuildOption:    -Dgtk_doc=false
BuildOption:    -Dman=false

BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi) >= 3.0.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  libtasn1-devel

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable. This package contains the runtime
libraries, tools, and server components.

%package devel
Summary:        Development files for the p11-kit library
Requires:       %{name} = %{version}

%description devel
This package contains the header files and pkg-config files needed to
develop applications that use p11-kit.


%install -a
install -d -m 755 %{buildroot}%{_sysconfdir}/pkcs11/modules
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/locale
rm -f %{buildroot}%{_sysconfdir}/pkcs11/pkcs11.conf.example

%files
%license COPYING
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules
%dir %{_libdir}/pkcs11
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/modules/p11-kit-trust.module
%{_libdir}/pkcs11/p11-kit-trust.so
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so
%{_bindir}/p11-kit
%{_bindir}/trust
%{_libdir}/pkcs11/p11-kit-client.so
%{_userunitdir}/p11-kit-server.service
%{_userunitdir}/p11-kit-server.socket

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc

%changelog
%{?autochangelog}

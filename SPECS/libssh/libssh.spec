# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# If we want to enable building pkcs11, change this to 1
%bcond pkcs11 0
%bcond gssapi 0

Name:           libssh
Version:        0.11.3
Release:        %autorelease
Summary:        A library implementing the SSH protocol
License:        LGPL-2.1-or-later
URL:            http://www.libssh.org
#!RemoteAsset
Source0:        https://www.libssh.org/files/0.11/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.libssh.org/files/0.11/%{name}-%{version}.tar.xz.asc
Source2:        libssh_client.config
Source3:        libssh_server.config
BuildSystem:    cmake

# We need sshd to run some tests
BuildOption(conf):  -DUNIT_TESTING=OFF
BuildOption(conf):  -DCLIENT_TESTING=OFF
BuildOption(conf):  -DSERVER_TESTING=OFF
%if %{with gssapi}
BuildOption(conf):  -DGSSAPI_TESTING=ON
%else
BuildOption(conf):  -DWITH_GSSAPI=OFF
%endif
%if %{with pkcs11}
BuildOption(conf):  -DWITH_PKCS11_URI=ON
BuildOption(conf):  -DWITH_PKCS11_PROVIDER=ON
%endif

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if %{with gssapi}
BuildRequires:  krb5-devel
%endif
BuildRequires:  cmocka-cmake
BuildRequires:  pam_wrapper
BuildRequires:  socket_wrapper
BuildRequires:  nss_wrapper
BuildRequires:  uid_wrapper
BuildRequires:  priv_wrapper
%if %{with pkcs11}
BuildRequires:  pkcs11-provider
BuildRequires:  p11-kit-devel
BuildRequires:  p11-kit-server
BuildRequires:  opensc
BuildRequires:  softhsm
BuildRequires:  gnutls
%endif

Requires:       %{name}-config = %{version}-%{release}

# Please Enable this back once we have crypto-policies
#Recommends:     crypto-policies


%description
The ssh library was designed to be used by programmers needing a working SSH
implementation by the mean of a library. The complete control of the client is
made by the programmer. With libssh, you can remotely execute programs, transfer
files, use a secure and transparent tunnel for your remote programs. With its
Secure FTP implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package config
Summary:        Configuration files for %{name}
BuildArch:      noarch

%description config
The %{name}-config package provides the default configuration files for %{name}.

%install -a
install -d -m755 %{buildroot}%{_sysconfdir}/libssh
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/libssh/libssh_client.config
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libssh/libssh_server.config

%files
%doc AUTHORS BSD CHANGELOG README
%license COPYING
%{_libdir}/libssh.so.4*

%files devel
%{_includedir}/libssh/
%{_libdir}/cmake/libssh/
%{_libdir}/pkgconfig/libssh.pc
%{_libdir}/libssh.so

%files config
%attr(0755,root,root) %dir %{_sysconfdir}/libssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_client.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_server.config

%changelog
%{?autochangelog}

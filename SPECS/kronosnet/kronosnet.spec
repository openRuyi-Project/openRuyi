# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kronosnet
Version:        1.33
Release:        %autorelease
Summary:        Multipoint-to-Multipoint VPN engine for clustering
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://kronosnet.org
VCS:            git:https://github.com/kronosnet/kronosnet.git
#!RemoteAsset:  sha256:638fb9bb8e689fa9fbfd6b364583988b8ef6453a277d46114e807b48f8c04674
Source:         %{url}/releases/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-libknet-sctp
BuildOption(conf):  --disable-libnozzle
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libqb-doxygen2man
BuildRequires:  libtool
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(zlib)

%description
Kronosnet is the new project name for libknet, a network abstraction
layer designed to multiplex multiple network links and provide both
encryption and compression of data passing on the wire.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared library symlinks and
pkg-config files needed to develop applications that link against
libknet.

%conf -p
autoreconf -fiv

%install -a
# remove duped documents
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# Upstream tests require live network interfaces and root capabilities
# that are not available inside the build chroot.

%files
%doc README README.licence
%license COPYING.applications COPYING.libraries COPYRIGHT
%{_libdir}/libknet.so.*
%dir %{_libdir}/kronosnet
%{_libdir}/kronosnet/crypto_nss.so
%{_libdir}/kronosnet/crypto_openssl.so
%{_libdir}/kronosnet/compress_bzip2.so
%{_libdir}/kronosnet/compress_lz4.so
%{_libdir}/kronosnet/compress_lz4hc.so
%{_libdir}/kronosnet/compress_lzma.so
%{_libdir}/kronosnet/compress_lzo2.so
%{_libdir}/kronosnet/compress_zlib.so
%{_libdir}/kronosnet/compress_zstd.so

%files devel
%{_includedir}/libknet.h
%{_libdir}/libknet.so
%{_libdir}/pkgconfig/libknet.pc
%{_mandir}/man3/knet_*.3*

%changelog
%autochangelog

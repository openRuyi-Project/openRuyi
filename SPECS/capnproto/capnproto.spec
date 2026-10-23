# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           capnproto
Version:        1.5.0
Release:        %autorelease
Summary:        Data interchange format and capability-based RPC system
License:        MIT
URL:            https://capnproto.org/
VCS:            git:https://github.com/capnproto/capnproto.git
#!RemoteAsset:  sha256:77dbc13ca82d9c87ddb4581dd49559d45b63096433d3dadea08b7f31b360a5ba
Source0:        https://capnproto.org/capnproto-c++-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n capnproto-c++-%{version}
BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

Provides:       %{name}-libs = %{version}-%{release}

%description
Cap'n Proto provides a schema compiler, a binary serialization format, and
a capability-based RPC system. This package contains the schema compiler,
standard schemas used by bindings for C++, Rust, and other languages,
and the Cap'n Proto and KJ runtime libraries.

%package        devel
Summary:        Development files for Cap'n Proto and KJ
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
C++ headers, linker symlinks, and pkg-config metadata for Cap'n Proto and KJ.

%conf -p
autoreconf -fiv

%install -a
find %{buildroot}%{_libdir} -name '*.la' -delete

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/capnp
%{_bindir}/capnpc
%{_bindir}/capnpc-capnp
%{_bindir}/capnpc-c++
%dir %{_includedir}/capnp
%dir %{_includedir}/capnp/compat
%{_includedir}/capnp/*.capnp
%{_includedir}/capnp/compat/*.capnp

# Cap'n Proto and KJ runtime libraries
%{_libdir}/libcapnp*-%{version}.so
%{_libdir}/libkj*-%{version}.so

%files devel
%dir %{_includedir}/capnp
%dir %{_includedir}/capnp/compat
%{_includedir}/capnp/*.h
%{_includedir}/capnp/compat/*.h
%{_includedir}/kj/
%{_libdir}/libcapnp.so
%{_libdir}/libcapnp-rpc.so
%{_libdir}/libcapnp-json.so
%{_libdir}/libcapnp-websocket.so
%{_libdir}/libcapnpc.so
%{_libdir}/libkj.so
%{_libdir}/libkj-test.so
%{_libdir}/libkj-async.so
%{_libdir}/libkj-http.so
%{_libdir}/libkj-tls.so
%{_libdir}/libkj-gzip.so
%{_libdir}/cmake/CapnProto/
%{_libdir}/pkgconfig/capnp.pc
%{_libdir}/pkgconfig/capnp-rpc.pc
%{_libdir}/pkgconfig/capnp-json.pc
%{_libdir}/pkgconfig/capnp-websocket.pc
%{_libdir}/pkgconfig/capnpc.pc
%{_libdir}/pkgconfig/kj.pc
%{_libdir}/pkgconfig/kj-test.pc
%{_libdir}/pkgconfig/kj-async.pc
%{_libdir}/pkgconfig/kj-http.pc
%{_libdir}/pkgconfig/kj-tls.pc
%{_libdir}/pkgconfig/kj-gzip.pc

%changelog
%autochangelog

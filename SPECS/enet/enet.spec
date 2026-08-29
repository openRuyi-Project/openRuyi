# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           enet
Version:        1.3.18
Release:        %autorelease
Summary:        ENet reliable UDP networking library
License:        MIT
URL:            http://sauerbraten.org/enet/
VCS:            git:https://github.com/lsalzman/enet
#!RemoteAsset:  sha256:28603c895f9ed24a846478180ee72c7376b39b4bb1287b73877e5eae7d96b0dd
Source:         https://github.com/lsalzman/enet/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
ENet's purpose is to provide a relatively thin,
simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary
feature it provides is optional reliable, in-order
delivery of packets. ENet omits certain higher level
networking features such as authentication, lobbying,
server discovery, encryption, or other similar tasks
that are particularly application specific so that the
library remains flexible, portable, and easily embeddable.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc ChangeLog README
%license LICENSE
%{_libdir}/libenet.so.*

%files devel
%doc docs/*.dox
%{_includedir}/enet/
%{_libdir}/libenet.so
%{_libdir}/pkgconfig/libenet.pc

%changelog
%autochangelog

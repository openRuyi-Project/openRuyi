# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zeromq
Version:        4.3.5
Release:        %autorelease
Summary:        Software library for fast, message-based applications
License:        MPL-2.0 AND BSD-3-Clause AND MIT
URL:            https://zeromq.org
#!RemoteAsset:  sha256:6653ef5910f17954861fe72332e68b03ca6e4d9c7160eb3a8de5a5a913bfab43
Source0:        https://github.com/%{name}/libzmq/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  xmlto
BuildRequires:  libsodium-devel

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.
This package contains the ZeroMQ shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# Remove bundled code.
rm -rf external/wepoll

# Fix permissions.
chmod -x src/xsub.hpp

%build
autoreconf -fi
%configure \
            --with-libsodium \
            --enable-drafts \
            --disable-Werror \
            --disable-static
%make_build

%install
%make_install

%files
%doc README.md AUTHORS NEWS
%license LICENSE
%{_bindir}/curve_keygen
%{_libdir}/libzmq.so.5*
%{_mandir}/man3/zmq_*
%{_mandir}/man7/zmq_*
%{_mandir}/man7/zmq.*

%files devel
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*.h

%changelog
%autochangelog

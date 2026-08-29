# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           librabbitmq
Version:        0.15.0
Release:        %autorelease
Summary:        Client library for AMQP 0-9-1 written in C
License:        MIT
URL:            https://github.com/alanxz/rabbitmq-c
#!RemoteAsset:  sha256:7b652df52c0de4d19ca36c798ed81378cba7a03a0f0c5d498881ae2d79b241c2
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/rabbitmq-c-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_API_DOCS:BOOL=OFF
BuildOption(conf):  -DBUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DBUILD_STATIC_LIBS:BOOL=OFF
BuildOption(conf):  -DBUILD_TESTING:BOOL=OFF
BuildOption(conf):  -DBUILD_TOOLS:BOOL=OFF
BuildOption(conf):  -DENABLE_SSL_SUPPORT:BOOL=ON
BuildOption(conf):  -DRUN_SYSTEM_TESTS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  pkgconfig(openssl)

%description
rabbitmq-c is a C-language AMQP 0-9-1 client library for use with v2.0+ of the
RabbitMQ broker. It is intended for client applications that want to publish
or consume messages over AMQP.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, shared library symlink, pkg-config
file and CMake config files needed to develop applications that link against
%{name}.

%prep
%autosetup -n rabbitmq-c-%{version}

%files
%doc README.md ChangeLog.md
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/amqp.h
%{_includedir}/amqp_framing.h
%{_includedir}/amqp_ssl_socket.h
%{_includedir}/amqp_tcp_socket.h
%{_includedir}/rabbitmq-c/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/librabbitmq.pc
%{_libdir}/cmake/rabbitmq-c/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           protobuf
Version:        33.2
Release:        %autorelease
Summary:        Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
URL:            https://github.com/protocolbuffers/protobuf
#!RemoteAsset:  sha256:6b6599b54c88d75904b7471f5ca34a725fa0af92e134dd1a32d5b395aa4b4ca8
Source0:        https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -Dprotobuf_BUILD_TESTS=OFF
BuildOption(conf):  -Dprotobuf_ABSL_PROVIDER=package

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(absl_absl_check)
BuildRequires:  pkgconfig(absl_absl_log)
BuildRequires:  pkgconfig(absl_algorithm)
BuildRequires:  pkgconfig(absl_base)
BuildRequires:  pkgconfig(absl_bind_front)
BuildRequires:  pkgconfig(absl_bits)
BuildRequires:  pkgconfig(absl_btree)
BuildRequires:  pkgconfig(absl_cleanup)
BuildRequires:  pkgconfig(absl_cord)
BuildRequires:  pkgconfig(absl_core_headers)
BuildRequires:  pkgconfig(absl_debugging)
BuildRequires:  pkgconfig(absl_die_if_null)
BuildRequires:  pkgconfig(absl_dynamic_annotations)
BuildRequires:  pkgconfig(absl_flags)
BuildRequires:  pkgconfig(absl_flat_hash_map)
BuildRequires:  pkgconfig(absl_flat_hash_set)
BuildRequires:  pkgconfig(absl_function_ref)
BuildRequires:  pkgconfig(absl_hash)
BuildRequires:  pkgconfig(absl_layout)
BuildRequires:  pkgconfig(absl_log_globals)
BuildRequires:  pkgconfig(absl_log_initialize)
BuildRequires:  pkgconfig(absl_log_severity)
BuildRequires:  pkgconfig(absl_memory)
BuildRequires:  pkgconfig(absl_node_hash_map)
BuildRequires:  pkgconfig(absl_node_hash_set)
BuildRequires:  pkgconfig(absl_optional)
BuildRequires:  pkgconfig(absl_random_distributions)
BuildRequires:  pkgconfig(absl_random_random)
BuildRequires:  pkgconfig(absl_span)
BuildRequires:  pkgconfig(absl_status)
BuildRequires:  pkgconfig(absl_statusor)
BuildRequires:  pkgconfig(absl_strings)
BuildRequires:  pkgconfig(absl_synchronization)
BuildRequires:  pkgconfig(absl_time)
BuildRequires:  pkgconfig(absl_type_traits)
BuildRequires:  pkgconfig(absl_utility)
BuildRequires:  pkgconfig(absl_variant)
BuildRequires:  pkgconfig(zlib)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libprotobuf-devel

%description    devel
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

%files
%license LICENSE
%{_libdir}/lib*.so*

%files devel
%license LICENSE
%doc CONTRIBUTORS.txt README.md
%{_bindir}/protoc*
%{_includedir}/google
%{_includedir}/upb
%{_includedir}/*.h
%{_libdir}/cmake/protobuf
%{_libdir}/cmake/utf8_range
%{_libdir}/pkgconfig/protobuf-lite.pc
%{_libdir}/pkgconfig/protobuf.pc
%{_libdir}/pkgconfig/upb.pc
%{_libdir}/pkgconfig/utf8_range.pc
# the UPB static lib is included, used for development
%{_libdir}/libupb.a

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global abi_version 0.2
%global temporal_features zoneinfo64,compiled_data,temporal_rs/float64_representable_durations

Name:           temporal-capi
Version:        0.2.6
Release:        %autorelease
Summary:        C and C++ interface to ECMAScript Temporal
License:        MIT OR Apache-2.0
URL:            https://github.com/boa-dev/temporal
VCS:            git:https://github.com/boa-dev/temporal.git
#!RemoteAsset:  sha256:f48eb9ca4ca22caaa48d1e7a534ad3fd598a23d1a71945e8ad5ac0be501fa5f2
Source0:        https://static.crates.io/crates/temporal_capi/%{version}/download#/%{name}-%{version}.tar.gz
Source1:        temporal_capi.pc.in
BuildSystem:    rust

BuildOption(build):  --lib --features %{temporal_features}

BuildRequires:  rust >= 1.86
BuildRequires:  cargo >= 1.86
BuildRequires:  rust-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  crate(diplomat-0.16) >= 0.16.0
BuildRequires:  crate(diplomat-runtime-0.15) >= 0.15.2
BuildRequires:  crate(icu-calendar-2) >= 2.2.1
BuildRequires:  crate(icu-locale-core-2/default) >= 2.1.0
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(temporal-rs-0.2) >= 0.2.6
BuildRequires:  crate(timezone-provider-0.2) >= 0.2.6
BuildRequires:  crate(writeable-0.6/default) >= 0.6.0
BuildRequires:  crate(temporal-rs-0.2/compiled-data) >= 0.2.6
BuildRequires:  crate(temporal-rs-0.2/float64-representable-durations) >= 0.2.6
BuildRequires:  crate(timezone-provider-0.2/zoneinfo64) >= 0.2.6
BuildRequires:  crate(zoneinfo64-0.3/default) >= 0.3.0

%description
C and C++ bindings for Temporal date, time, calendar and time zone operations.

%package        devel
Summary:        Development files for Temporal
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config metadata for the Temporal shared library.

%prep -a
sed -i '/^\[lib\]$/a crate-type = ["cdylib"]' Cargo.toml

%build -a
patchelf --set-soname libtemporal_capi.so.%{abi_version} target/release/libtemporal_capi.so

%install
install -D -m 755 target/release/libtemporal_capi.so %{buildroot}%{_libdir}/libtemporal_capi.so.%{abi_version}
ln -s libtemporal_capi.so.%{abi_version} %{buildroot}%{_libdir}/libtemporal_capi.so
install -d %{buildroot}%{_includedir}/temporal_capi/temporal_rs
install -m 644 bindings/c/*.h %{buildroot}%{_includedir}/temporal_capi/
install -m 644 bindings/cpp/temporal_rs/*.hpp %{buildroot}%{_includedir}/temporal_capi/temporal_rs/
install -D -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/temporal_capi.pc
sed -i -e 's|@PREFIX@|%{_prefix}|g' -e 's|@LIBDIR@|%{_libdir}|g' \
    -e 's|@INCLUDEDIR@|%{_includedir}|g' -e 's|@VERSION@|%{version}|g' \
    %{buildroot}%{_libdir}/pkgconfig/temporal_capi.pc

%check -p
export RUST_TEST_FLAGS="--release --features %{temporal_features}"

%check -a
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
export PKG_CONFIG_SYSROOT_DIR=%{buildroot}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{__cc} %{build_cflags} tests/c/simple.c $(pkg-config --cflags --libs temporal_capi) %{build_ldflags} -o c_test
./c_test
%{__cxx} %{build_cxxflags} -std=c++17 tests/cpp/simple.cpp $(pkg-config --cflags --libs temporal_capi) %{build_ldflags} -o cpp_test
./cpp_test

%files
%doc README.md
%license LICENSE-Apache LICENSE-MIT
%{_libdir}/libtemporal_capi.so.%{abi_version}

%files devel
%{_includedir}/temporal_capi/
%{_libdir}/libtemporal_capi.so
%{_libdir}/pkgconfig/temporal_capi.pc

%changelog
%autochangelog

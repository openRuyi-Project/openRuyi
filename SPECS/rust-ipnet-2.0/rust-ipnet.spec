# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ipnet
%global full_version 2.12.0
%global pkgname ipnet-2.0

Name:           rust-ipnet-2.0
Version:        2.12.0
Release:        %autorelease
Summary:        Rust crate "ipnet"
License:        MIT OR Apache-2.0
URL:            https://github.com/krisprice/ipnet
#!RemoteAsset:  sha256:d98f6fed1fde3f8c21bc40a1abb88dd75e67924f9cffc3ef95607bad8017f8e2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
Source code for takopackized Rust crate "ipnet"

%package     -n %{name}+heapless
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "heapless"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(heapless-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}/heapless)

%description -n %{name}+heapless
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "heapless" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "json"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/schemars08)
Requires:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/json)

%description -n %{name}+json
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "json" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars08
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "schemars08" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(schemars-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/schemars)
Provides:       crate(%{pkgname}/schemars08)

%description -n %{name}+schemars08
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "schemars08" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "schemars" feature.

%package     -n %{name}+schemars1
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "schemars1"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/schemars1)

%description -n %{name}+schemars1
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "schemars1" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ser-as-str
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "ser_as_str"
Requires:       crate(%{pkgname})
Requires:       crate(heapless-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}/ser-as-str)

%description -n %{name}+ser-as-str
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "ser_as_str" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.
This metapackage enables feature "serde" for the Rust ipnet crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name protobuf
%global full_version 2.28.0
%global pkgname protobuf-2

Name:           rust-protobuf-2
Version:        2.28.0
Release:        %autorelease
Summary:        Rust crate "protobuf"
License:        MIT
URL:            https://github.com/stepancheg/rust-protobuf/
#!RemoteAsset:  sha256:106dd99e98437432fed6519dedecfade6a06a73bb7b2a1e019fdd2bee5778d94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "protobuf"

%package     -n %{name}+bytes
Summary:        Google protocol buffers - feature "bytes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}
Provides:       crate(%{pkgname}/with-bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust protobuf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-bytes" feature.

%package     -n %{name}+serde
Summary:        Google protocol buffers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust protobuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Google protocol buffers - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
This metapackage enables feature "serde_derive" for the Rust protobuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        Google protocol buffers - feature "with-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust protobuf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

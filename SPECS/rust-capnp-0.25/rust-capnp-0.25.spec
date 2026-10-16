# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name capnp
%global full_version 0.25.6
%global pkgname capnp-0.25

Name:           rust-capnp-0.25
Version:        0.25.6
Release:        %autorelease
Summary:        Rust crate "capnp"
License:        MIT
URL:            https://github.com/capnproto/capnproto-rust
#!RemoteAsset:  sha256:4777a3bc19b8f8e5fb2d0196c6b5dfcbbcc8b2fe08ae57f873f2f35f15cfc210
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/rpc-try) = %{version}
Provides:       crate(%{pkgname}/sync-reader) = %{version}
Provides:       crate(%{pkgname}/unaligned) = %{version}

%description
Source code for takopackized Rust crate "capnp"

%package     -n %{name}+alloc
Summary:        Runtime library for Cap'n Proto data encoding - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.7/alloc) >= 0.7.1
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust capnp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Runtime library for Cap'n Proto data encoding - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust capnp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+embedded-io
Summary:        Runtime library for Cap'n Proto data encoding - feature "embedded-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.7) >= 0.7.1
Provides:       crate(%{pkgname}/embedded-io) = %{version}

%description -n %{name}+embedded-io
This metapackage enables feature "embedded-io" for the Rust capnp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Runtime library for Cap'n Proto data encoding - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust capnp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Runtime library for Cap'n Proto data encoding - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embedded-io-0.7/std) >= 0.7.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust capnp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

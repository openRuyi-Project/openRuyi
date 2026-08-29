# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ruzstd
%global full_version 0.8.3
%global pkgname ruzstd-0.8

Name:           rust-ruzstd-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "ruzstd"
License:        MIT
URL:            https://github.com/KillingSpark/zstd-rs
#!RemoteAsset:  sha256:a7c1c839d570d835527c9a5e4db7cb2198683a988cb9d7293fc8674e6bd58fc8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/fuzz-exports) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ruzstd"

%package     -n %{name}+default
Summary:        Decoder for the zstd compression format - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hash) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ruzstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dict-builder
Summary:        Decoder for the zstd compression format - feature "dict_builder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(fastrand-2/default) >= 2.3.0
Provides:       crate(%{pkgname}/dict-builder) = %{version}

%description -n %{name}+dict-builder
This metapackage enables feature "dict_builder" for the Rust ruzstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash
Summary:        Decoder for the zstd compression format - feature "hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(twox-hash-2/xxhash64) >= 2.0.0
Provides:       crate(%{pkgname}/hash) = %{version}

%description -n %{name}+hash
This metapackage enables feature "hash" for the Rust ruzstd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Decoder for the zstd compression format - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust ruzstd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

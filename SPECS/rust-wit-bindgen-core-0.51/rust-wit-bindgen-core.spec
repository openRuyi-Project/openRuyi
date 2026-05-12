# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen-core
%global full_version 0.51.0
%global pkgname wit-bindgen-core-0.51

Name:           rust-wit-bindgen-core-0.51
Version:        0.51.0
Release:        %autorelease
Summary:        Rust crate "wit-bindgen-core"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:ea61de684c3ea68cb082b7a88508a8b27fcc8b797d738bfc99a82facf1d752dc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(wit-parser-0.244/default) >= 0.244.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wit-bindgen-core"

%package     -n %{name}+clap
Summary:        Low-level support for bindings generation based on WIT files for use with `wit-bindgen-cli` and other languages - feature "clap"
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/default) >= 4.3.19
Requires:       crate(clap-4.0/derive) >= 4.3.19
Provides:       crate(%{pkgname}/clap)

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust wit-bindgen-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Low-level support for bindings generation based on WIT files for use with `wit-bindgen-cli` and other languages - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.218
Requires:       crate(serde-1.0/derive) >= 1.0.218
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wit-bindgen-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

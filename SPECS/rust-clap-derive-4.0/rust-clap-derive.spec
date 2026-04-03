# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_derive
%global full_version 4.6.0
%global pkgname clap-derive-4.0

Name:           rust-clap-derive-4.0
Version:        4.6.0
Release:        %autorelease
Summary:        Rust crate "clap_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:1110bd8a634a1ab8cb04345d8d878267d57c3cf1b38d91b71af6686408bbca6a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/deprecated)
Provides:       crate(%{pkgname}/raw-deprecated)
Provides:       crate(%{pkgname}/unstable-v5)

%description
Source code for takopackized Rust crate "clap_derive"

%package     -n %{name}+unstable-markdown
Summary:        Parse command line argument by defining a struct, derive crate - feature "unstable-markdown"
Requires:       crate(%{pkgname})
Requires:       crate(anstyle-1.0/default) >= 1.0.13
Requires:       crate(pulldown-cmark-0.13) >= 0.13.1
Provides:       crate(%{pkgname}/unstable-markdown)

%description -n %{name}+unstable-markdown
This metapackage enables feature "unstable-markdown" for the Rust clap_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

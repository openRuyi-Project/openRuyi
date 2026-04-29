# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-trace
%global full_version 0.1.18
%global pkgname gix-trace-0.1

Name:           rust-gix-trace-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "gix-trace"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:f69a13643b8437d4ca6845e08143e847a36ca82903eed13303475d0ae8b162e0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/tracing-detail)

%description
Source code for takopackized Rust crate "gix-trace"

%package     -n %{name}+document-features
Summary:        Provide minimal `tracing` support that can be turned off to zero cost - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-trace crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Provide minimal `tracing` support that can be turned off to zero cost - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust gix-trace crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

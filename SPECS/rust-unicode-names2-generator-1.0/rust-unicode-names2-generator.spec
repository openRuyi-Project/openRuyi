# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode_names2_generator
%global full_version 1.3.0
%global pkgname unicode-names2-generator-1.0

Name:           rust-unicode-names2-generator-1.0
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "unicode_names2_generator"
License:        MIT OR Apache-2.0
URL:            https://github.com/progval/unicode_names2
#!RemoteAsset:  sha256:b91e5b84611016120197efd7dc93ef76774f4e084cd73c9fb3ea4a86c570c56e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getopts-0.2/default) >= 0.2.21
Requires:       crate(log-0.0.0/default) >= 0.0.0
Requires:       crate(phf-codegen-0.11/default) >= 0.11.1
Requires:       crate(rand-0.8/default) >= 0.8.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "unicode_names2_generator"

%package     -n %{name}+time
Summary:        Generates the perfect-hash function used by `unicode_names2` - feature "time" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/timing)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust unicode_names2_generator crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "timing" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x86
%global full_version 0.52.0
%global pkgname x86-0.52

Name:           rust-x86-0.52
Version:        0.52.0
Release:        %autorelease
Summary:        Rust crate "x86"
License:        MIT
URL:            https://github.com/gz/rust-x86
#!RemoteAsset:  sha256:2781db97787217ad2a2845c396a5efe286f87467a5810836db6d74926e94a385
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-field-0.10/default) >= 0.10.1
Requires:       crate(bitflags/default)
Requires:       crate(raw-cpuid-10/default) >= 10.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/utest) = %{version}
Provides:       crate(%{pkgname}/vmtest) = %{version}

%description
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
Source code for takopackized Rust crate "x86"

%package     -n %{name}+csv
Summary:        Program x86 (amd64) hardware - feature "csv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(csv-1/default) >= 1.1.5
Provides:       crate(%{pkgname}/csv) = %{version}

%description -n %{name}+csv
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
This metapackage enables feature "csv" for the Rust x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+performance-counter
Summary:        Program x86 (amd64) hardware - feature "performance-counter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/csv) = %{version}
Requires:       crate(%{pkgname}/phf) = %{version}
Requires:       crate(%{pkgname}/phf-codegen) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/performance-counter) = %{version}

%description -n %{name}+performance-counter
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
This metapackage enables feature "performance-counter" for the Rust x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        Program x86 (amd64) hardware - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
This metapackage enables feature "phf" for the Rust x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf-codegen
Summary:        Program x86 (amd64) hardware - feature "phf_codegen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-codegen-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/phf-codegen) = %{version}

%description -n %{name}+phf-codegen
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
This metapackage enables feature "phf_codegen" for the Rust x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Program x86 (amd64) hardware - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.61
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
Contains x86 specific data structure descriptions, data-tables, as well as convenience function to call assembly instructions typically not exposed in higher level languages.
This metapackage enables feature "serde_json" for the Rust x86 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

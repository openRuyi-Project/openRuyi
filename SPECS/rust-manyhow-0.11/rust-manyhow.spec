# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name manyhow
%global full_version 0.11.4
%global pkgname manyhow-0.11

Name:           rust-manyhow-0.11
Version:        0.11.4
Release:        %autorelease
Summary:        Rust crate "manyhow"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/manyhow
#!RemoteAsset:  sha256:b33efb3ca6d3b07393750d4030418d594ab1139cee518f0dc88db70fec873587
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "manyhow"

%package     -n %{name}+darling-core
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "darling_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.20/default) >= 0.20.1
Provides:       crate(%{pkgname}/darling)
Provides:       crate(%{pkgname}/darling-core)

%description -n %{name}+darling-core
This metapackage enables feature "darling_core" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "darling" feature.

%package     -n %{name}+default
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/syn)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(manyhow-macros-0.11/default) >= 0.11.4
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn1
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "syn1"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/printing) >= 2.0.117
Provides:       crate(%{pkgname}/syn1)

%description -n %{name}+syn1
This metapackage enables feature "syn1" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn2
Summary:        Proc macro error handling à la anyhow x proc-macro-error - feature "syn2" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Provides:       crate(%{pkgname}/syn)
Provides:       crate(%{pkgname}/syn2)

%description -n %{name}+syn2
This metapackage enables feature "syn2" for the Rust manyhow crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syn" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

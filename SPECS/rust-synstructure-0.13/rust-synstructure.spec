# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name synstructure
%global full_version 0.13.2
%global pkgname synstructure-0.13

Name:           rust-synstructure-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "synstructure"
License:        MIT
URL:            https://github.com/mystor/synstructure
#!RemoteAsset:  sha256:728a70f3dbaf5bab7f0c4b1ac8d7ae5ea60a4b5549c8a5914361c99147a709d2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "synstructure"

%package     -n %{name}+proc-macro
Summary:        Helper methods and macros for custom derives - feature "proc-macro" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.106
Requires:       crate(quote-1.0/proc-macro) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/proc-macro) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/proc-macro)

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust synstructure crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

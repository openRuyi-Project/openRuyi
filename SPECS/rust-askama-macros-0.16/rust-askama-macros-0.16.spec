# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name askama_macros
%global full_version 0.16.1
%global pkgname askama-macros-0.16

Name:           rust-askama-macros-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "askama_macros"
License:        MIT OR Apache-2.0
URL:            https://askama.rs/
#!RemoteAsset:  sha256:643e1c7cbb6aec1d920332fe51a7c0d8219e273dcb8602db03f5263e4d16487b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description
Source code for takopackized Rust crate "askama_macros"

%package     -n %{name}+alloc
Summary:        Procedural macro package for Askama - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/alloc) >= 0.16.1
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+code-in-doc
Summary:        Procedural macro package for Askama - feature "code-in-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/code-in-doc) >= 0.16.1
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Provides:       crate(%{pkgname}/code-in-doc) = %{version}

%description -n %{name}+code-in-doc
This metapackage enables feature "code-in-doc" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+config
Summary:        Procedural macro package for Askama - feature "config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/config) >= 0.16.1
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Provides:       crate(%{pkgname}/config) = %{version}

%description -n %{name}+config
This metapackage enables feature "config" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Procedural macro package for Askama - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/config) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/urlencode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Procedural macro package for Askama - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/code-in-doc) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-spans
Summary:        Procedural macro package for Askama - feature "nightly-spans"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/nightly-spans) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Provides:       crate(%{pkgname}/nightly-spans) = %{version}

%description -n %{name}+nightly-spans
This metapackage enables feature "nightly-spans" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Procedural macro package for Askama - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Requires:       crate(askama-derive-0.16/serde-json) >= 0.16.1
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Procedural macro package for Askama - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Requires:       crate(askama-derive-0.16/std) >= 0.16.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+urlencode
Summary:        Procedural macro package for Askama - feature "urlencode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-derive-0.16/external-sources) >= 0.16.1
Requires:       crate(askama-derive-0.16/proc-macro) >= 0.16.1
Requires:       crate(askama-derive-0.16/urlencode) >= 0.16.1
Provides:       crate(%{pkgname}/urlencode) = %{version}

%description -n %{name}+urlencode
This metapackage enables feature "urlencode" for the Rust askama_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
